import java.util.Scanner;
import java.util.Stack;

public class bracket {

	public static void main(String[] args) {
		Stack<Character> stack = new Stack<>();
		Scanner sc = new Scanner(System.in);
		char testCh, openPair;
		int count = 0;
		boolean isPair = true;

		count = sc.nextInt();
		sc.nextLine();
		String[] bracket = new String[count], result = new String[count];

		for (int i = 0; i < count; i++) {
			bracket[i] = sc.nextLine();
		}

		for (int i = 0; i < bracket.length; i++) {
			isPair = true;
			stack.clear();
			for (int j = 0; j < bracket[i].length(); j++) {
				testCh = bracket[i].charAt(j);
				switch (testCh) {
				case '(':
				case '{':
				case '[':
					stack.push(testCh);
					break;

				case ')':
				case '}':
				case ']':
					if (stack.isEmpty()) {
						isPair = false;
						break;
					} else {
						openPair = stack.pop();
						if ((openPair == '(') && (testCh != ')') || (openPair == '{') && (testCh != '}')
								|| (openPair == '[') && (testCh != ']')) {
							isPair = false;
						}
					}
				}
			}
			if(isPair) {
				result[i] = "YES";
			} else {
				result[i] = "No";
			}
		}
		for(int i = 0; i<result.length; i++) {
			System.out.println(result[i]);
		}
	}
}
