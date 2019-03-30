// https://www.acmicpc.net/problem/1924 - Excercise URL

import java.util.*;
import java.lang.*;
import java.io.*;

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);

		int month=0,day=0,sum=0,sum1=0;
		int[] month_array = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		String[] week= {"SUN","MON", "TUE", "WED", "THU", "FRI", "SAT"};

		month = sc.nextInt();
		day = sc.nextInt();

		for(int i=0; i<month; i++){
			sum += month_array[i];
		}
		sum += day;
		sum1 = sum % 7;

		System.out.println(week[sum1]);
	}
}
