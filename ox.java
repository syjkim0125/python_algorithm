// Exercise Address https://www.acmicpc.net/problem/8958
import java.util.Scanner;

public class ox {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int result = 0, count = 0, numCount = 0;

		count = sc.nextInt();
		sc.nextLine();

		String[] ox = new String[count];

		for(int i = 0; i < count; i++) {
			ox[i] = sc.nextLine();
		}

		for(int i = 0; i < count; i++) {
			result = 0;
			numCount = 0;
			for(int j = 0; j < ox[i].length(); j++) {
				if(ox[i].charAt(j) == 'O'){
					numCount++;
					result += numCount;
				}
				else {
					numCount = 0;
				}
			}
			System.out.println(result);
		}
	}
}
