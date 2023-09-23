import java.util.*;
public class NonRestoring{
    public static void main(String args[]){
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter Dividend:");
        int a = sc.nextInt(); 
        
        System.out.println("Enter Divisor:");
        int b = sc.nextInt(); 

        String m =binary(a);
        String m1 =binary(b);

        int x = m.length();
        int y = m1.length();
        
        String A="";
		for (int i = 0; i < x+1; i++) {
			A = A + "0";
		} 
        if(A.length()!=x){
        for (int i = 0; i < A.length()-y; i++) {
			m1 = "0"+m1;
		} 
    }
        System.out.println("Binary Dividend(Q):"+m);
		System.out.println("Binary Divisor(M):"+m1);
        int count =x;
        while(count>0){
            System.out.println("\n");
            System.out.println("Count:"+count);
            A=A.substring(1)+m.charAt(0);
            m=m.substring(1);
			System.out.println("\nA:"+A);
            System.out.println("\nQ:"+m);
            if(A.charAt(0)=='0')
            {
                A=binaryadd(A,get2scomplement(m1));                
            }
            else
            {
                A=binaryadd(A,m1);
            }
            if(A.charAt(0)=='0')
            {
                m=m+"1";
            }
            else{
                m=m+"0";
            }
            System.out.println("\nA:"+A);
            System.out.println("\nQ:"+m);
            count=count-1;
    }
    if(A.charAt(0)=='1')
    {
        A=binaryadd(A,m1);                
    }
    System.out.println("\nBinary Quotient:"+m);
    System.out.println("\nBinary Remainder:"+A);
    System.out.println("\nDecimal Quotient:"+binarytodec(m));
    System.out.println("\nDecimal Remainder:"+binarytodec(A));
    }


public static String get2scomplement(String s1)
{
    //1's complement
    String s2 = "";
		for (int i = 0; i < s1.length(); i++) { 

			if (s1.charAt(i) == '0') {
				s2 += '1';
				continue;
			}
			s2 += '0';
		}
        String s3 = "";
		String carry = "1";
		for (int i = s2.length() - 1; i >= 0; i--) {

			if (s2.charAt(s2.length() - 1) == '0') {
				s2 = s2.substring(0, s2.length() - 1) + "1";
				return s2;
			}

			if (s2.charAt(i) == '1' && carry.equals("1")) {
				s3 = '0' + s3;
				carry = "1";
			} else if (s2.charAt(i) == '0' && carry.equals("1")) {
				s3 = '1' + s3;
				carry = "0";
			} else if (s2.charAt(i) == '0' && carry.equals("0")) {
				s3 = '0' + s3;
				carry = "0";
			} else {
				s3 = '1' + s3;
				carry = "0";
			}

		}

		return s3;
}
public static String binary(int n)
{
    String s1 = "";
        s1 = Integer.toBinaryString(n);
		return s1;
}
    public static Long binarytodec(String s) {
		Long n = Long.parseLong(s);
		Long rem = (long) 0;
		Long ans = (long) 0;
		Long val = (long) 1;

		while (n != 0) {
			rem = n % 10;
			ans = ans + rem * val;
			n = n / 10;
			val = val * 2;

		}
		return ans;

	}
    public static String binaryadd(String s1, String s2) {
        int x,y;
        if(!s1.equals(s2))
        {
            x=s1.length();
            y=s2.length();
            int c=0;
        if(x>y){
        c=x;
        for (int i = 0; i < c-y ; i++) {
			s2= "0"+s2;
		}
        }
        else{
        c=y;
        for (int i = 0; i < c-x ; i++) {
			s1 = "0"+s1;
		} 
        } 
        }
		String res = "";
		String carry = "0";
		for (int i = s1.length() - 1; i >= 0; i--) {

			if (s1.charAt(i) == '1' && s2.charAt(i) == '1' && carry.equals("0")
					|| (s1.charAt(i) == '0' && s2.charAt(i) == '1' && carry.equals("1"))
					|| s1.charAt(i) == '1' && s2.charAt(i) == '0' && carry.equals("1")) {
				res = '0' + res;
				carry = "1";
			} else if (s1.charAt(i) == '1' && s2.charAt(i) == '1' && carry.equals("1")) {
				res = '1' + res;
				carry = "1";
			} else if (s1.charAt(i) == '0' && s2.charAt(i) == '1' && carry.equals("0")
					|| s1.charAt(i) == '1' && s2.charAt(i) == '0' && carry.equals("0")
					|| s1.charAt(i) == '0' && s2.charAt(i) == '0' && carry.equals("1")) {
				res = '1' + res;
				carry = "0";
			} else if (s1.charAt(i) == '0' && s2.charAt(i) == '0' && carry.equals("0")) {
				res = '0' + res;
				carry = "0";
			}

		}

		return res;

	}
}