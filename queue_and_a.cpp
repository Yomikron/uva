#include <stdio.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <sstream>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <ctype.h>
#include <functional>
using namespace std;

struct Staff {
    int staffId;
    vector<int> expertise;
    bool operator<(const Staff &x) const {
        return staffId < x.staffId;
    }
};

struct Task {
    int topicId, startTime, serviceTime;
    Task(int t = 0, int s = 0, int e = 0):
    topicId(t), startTime(s), serviceTime(e) {}
};

struct cmpTask {
    bool operator() (const Task &a, const Task &b) const {
        return a.startTime > b.startTime;
    }
};

bool cmp(pair<int, int> a, pair<int, int> b) {
    if (a.first != b.first) return a.first < b.first;
    return a.second < b.second;
}

int main() {
    int N, M, scenario = 0;
    while (scanf("%d", &N) == 1 && N) {
		// dictionary which contains for each topic a priority queues of related tasks
        map<int, priority_queue<Task, vector<Task>, cmpTask> > scheduler;
		// timeline when any task can be allocated
        priority_queue<int, vector<int>, greater<int> > timeline;
        for (int i = 0; i < N; i++) {
            int topicId, num, t0, t, deltaTime;
            scanf("%d %d %d %d %d", &topicId, &num, &t0, &t, &deltaTime);
            for (int j = 0; j < num; j++) {
                scheduler[topicId].push(Task(topicId, t0, t));
                timeline.push(t0);
                t0 += deltaTime;
            }
        }
        scanf("%d", &M);
        Staff staffs[5];

        for (int i = 0; i < M; i++) {
            int staffId, num, topicId;
            scanf("%d %d", &staffId, &num);
            staffs[i].staffId = staffId;
            for (int j = 0; j < num; j++) {
                scanf("%d", &topicId);
                staffs[i].expertise.push_back(topicId);
            }
        }
		// sort by staffId
        sort(staffs, staffs+M); 
        int working[5] = {}, previousRequest[5] = {}, finalRequest[5] = {};
        int totalTime = -2, now;
        timeline.push(-1);
		// work through timeline
        while (!timeline.empty()) {
            now = timeline.top();
            timeline.pop();
			
            if (now == totalTime)
                continue;
            totalTime = now;
			
            for (int i = 0; i < M; i++) {
                if (working[i] && finalRequest[i] <= now)
                    working[i] = 0;
            }
            vector< pair<int, int> > available;
            for (int i = 0; i < M; i++) {
                if (working[i] == 0) {
                    available.push_back(make_pair(previousRequest[i], i));
                }
            }
            sort(available.begin(), available.end(), cmp);
            for (int i = 0; i < available.size(); i++) {
				// pick prioritised worker from queue 
                Staff &u = staffs[available[i].second];
                for (int j = 0; j < u.expertise.size(); j++) {
					// pick prioritised skill from worker
                    int topicId = u.expertise[j];
                    if (!scheduler[topicId].empty()) {
                        Task tmp = scheduler[topicId].top();
                        if (tmp.startTime <= now) {
                            scheduler[topicId].pop();
                            previousRequest[available[i].second] = now;
                            finalRequest[available[i].second] = now + tmp.serviceTime;
                            working[available[i].second] = 1;
                            timeline.push(finalRequest[available[i].second]);
                            break;
                        }
                    }
                }
            }
        }
        printf("Scenario %d: All requests are serviced within %d minutes.\n", ++scenario, totalTime);
    }
    return 0;
}