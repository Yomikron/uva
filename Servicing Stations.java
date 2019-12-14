import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	static Boolean connected[][] = new Boolean[40][40];
	static int towns;
	static int minDominatingSet;
	static List<Boolean> visited = new ArrayList<Boolean>();
	static int maximumTownNumber[] = new int[40];
	

	static void dfs(int currentTown, int reachableTowns, int stationsCount) {
		// prune when the number
		if (stationsCount >= minDominatingSet) {
			return;
		}
		for (int i = 1; i < currentTown; i++) {
			if (!visited.get(i) && maximumTownNumber[i] < currentTown) {
				return;
			}
		}
		
		// found possible solution
		if (reachableTowns == towns) {
			minDominatingSet = stationsCount;
		}
		
		
		// go to the next town
		dfs(currentTown + 1, reachableTowns, stationsCount);
		
		// check if there are any new towns we can visit now from the current town
		int temp[] = new int[40]; 
		int a = 0;
		for (int i = 1; i <= towns; i++) {
			if (connected[currentTown][i] && !visited.get(i)) {
				visited.set(i, true);
				temp[a++] = i;
			}
		}
		if (a == 0) {
			return;
		}
		
		// go deeper
		dfs(currentTown + 1, reachableTowns + a, stationsCount + 1); 
		
		// reset visited towns
		for (int i = 0; i < a; i++) {
			visited.set(temp[i], false);
		}
	}
	
	public static void main(String[] args) throws FileNotFoundException {
		Scanner s = new Scanner(System.in);
		int edges;
		
		while (true) {
			towns = s.nextInt();
			edges = s.nextInt();
			
			// end of test
			if(edges==0 && towns==0) {
				break;
			}
			
			visited.clear();
			for (int i = 1; i <= towns+1; i++) {
				visited.add(false);
				maximumTownNumber[i] = 0;
			}
			for (int i = 1; i <= towns+1; i++) {
				for (int j = 1; j <= towns+1; j++)
					connected[i][j] = false;
				connected[i][i] = true; 
			}
			minDominatingSet = towns;
			
			// fill data grid
			for (int i = 0; i < edges; i++) {
				int a = s.nextInt();
				int b = s.nextInt();
				connected[a][b] = true;
				connected[b][a] = true;
			}
			// set maximum town number of neighbors
			for (int i = 1; i <= towns; i++) {
				for (int j = 1; j <= towns; j++) {
					if (connected[i][j] && maximumTownNumber[i] < j) {
						maximumTownNumber[i] = j; 
					}
				}
			}
			// start searching
			dfs(1, 0, 0);
			System.out.println(minDominatingSet);
		}
		s.close();
	}

}
