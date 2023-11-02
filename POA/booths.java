import java.util.*;
public class booths{
    public static void main(String args[]){
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter Multiplicand:");
        int a = sc.nextInt(); 
        
        System.out.println("Enter Multiplier:");
        int b = sc.nextInt(); 
        String m =binary(a);
        String m1 =binary(b);
        int x = m.length();
        int y = m1.length();
        int c=0;
		if(x>y)
        c=x;
		else
		c=y;
		if(a>0)
		{
			for (int i = 0; i < c-x ; i++) {
			m = "0"+m;
		} 
		}
		else{
			for (int i = 0; i < c-x ; i++) {
			m = "1"+m;
		} 
		}
		if(b>0)
		{
			for (int i = 0; i < c-y ; i++) {
			m1 = "0"+m1;
		} 
		}
		else{
			for (int i = 0; i < c-y ; i++) {
			m1 = "1"+m1;
		} 
		}
        System.out.println("Binary Multiplicand(M):"+m);
		System.out.println("Binary Multiplier(M1):"+m1);
        String A="";
		for (int i = 0; i < c; i++) {
			A = A + "0";
		} 
        System.out.println("\nAC:"+A);
        String q1="0";
        char q= m1.charAt(c-1);
        String qq1=q+q1;
        System.out.println("\nQQ1:"+qq1);
        int count =c;
        while(count>0){
            System.out.println("\n");
            System.out.println("Iteration:"+count);
        if(qq1.equals("10")){
        String minusm=get2scomplement(m);
        A=binaryadd(A,minusm);
        System.out.println("\nAC:"+A);
        q1=shiftrightq1(m1,q1);
        m1=shiftrightq(A,m1);
        A=shiftrightac(A);
        System.out.println("\nAC:"+A);
        System.out.println("\nQ:"+m1);
        System.out.println("\nq1:"+q1);
        }
        else if(qq1.equals("01")){
        A=binaryadd(A,m);
        System.out.println("\nAC:"+A);
        q1=shiftrightq1(m1,q1);
        m1=shiftrightq(A,m1);
        A=shiftrightac(A);
        System.out.println("\nAC:"+A);
        System.out.println("\nQ:"+m1);
        System.out.println("\nq1:"+q1);
        }
        else if(qq1.equals("00")||qq1.equals("11")){
            q1=shiftrightq1(m1,q1);
        m1=shiftrightq(A,m1);
        A=shiftrightac(A);
        System.out.println("\nAC:"+A);
        System.out.println("\nQ:"+m1);
        System.out.println("\nq1:"+q1);
        }
         q= m1.charAt(c-1);
         qq1=q+q1;
         System.out.println("qq1:"+qq1);
         System.out.println("\n");
        count=count-1;
        }
        String multiply=A+m1;
        String mul=multiply;
        System.out.println("Binary ans:"+multiply);
        if(multiply.charAt(0)== '1'){
            mul = get2scomplement(multiply);
        }
        Long dec;
     dec=binarytodec(mul);
    if(multiply.charAt(0)== '1')
    System.out.println("Decimal ans:-"+dec);
    else
    System.out.println("Decimal ans:"+dec);
    }


public static String get2scomplement(String s1)
{
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
    if(n>=0)
    {
        s1 = Integer.toBinaryString(n);
        s1 = "0"+s1;
    } else {
			s1 = Integer.toBinaryString(-1 * n);
			s1 = get2scomplement(s1);
			s1 = "1" + s1;
		}
		return s1;
}
public static String shiftrightac(String str) {

		return str.charAt(0) + str.substring(0, str.length() - 1);

	}
	public static String shiftrightq(String str,String str1) {
	    int x=str.length();
	    int c = str.charAt(x-1);
        if(c==49)
        {
		return 1 + str1.substring(0, str1.length() - 1);}
		else{
		return 0 + str1.substring(0, str1.length() - 1);
		}

	}
	public static String shiftrightq1(String str,String str1) {
	    int x=str.length();
	    int c = str.charAt(x-1);
        if(c==49)
        {
            str1="1";
		return str1;}
		else{
		    str1="0";
		return str1 ;
		}

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