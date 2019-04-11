package test_java;
import java.util.Scanner;
import java.util.ArrayList;

public class pangram {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<String> inputString = new ArrayList<>();
		int[] check_array = new int[26];
		int count = 0;
		boolean check = true;
		String result = "";

		count = sc.nextInt();
		sc.nextLine();

		for(int i=0; i<count; i++) {
			check = true;
			check_array = new int[26];
			inputString.add(sc.nextLine());
			for(int j=0; j<inputString.get(i).length(); j++) {
				//System.out.println(inputString.get(i).charAt(j) - 'a');
				if(inputString.get(i).charAt(j) - 'a' >= 0 && inputString.get(i).charAt(j) - 'a' <= 26) {
					check_array[inputString.get(i).charAt(j) - 'a'] = 1;
				}
			}

			for(int k=0; k<check_array.length; k++) {
				//System.out.println(check_array[k]);
				if(check_array[k] != 1) {
					check = false;
					break;
				}
			}
			if(check) {
				result += "1";
			} else {
				result += "0";
			}
		}
		System.out.println(result);
	}
}
