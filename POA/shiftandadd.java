import java.util.*;
public class shiftandadd{
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
        if(x>y){
        c=x;
        for (int i = 0; i < c-y ; i++) {
			m1= "0"+m1;
		}
        }
        else{
        c=y;
        for (int i = 0; i < c-x ; i++) {
			m = "0"+m;
		} 
        } 
        System.out.println("Binary Multiplicand(M):"+m);
		System.out.println("Binary Multiplier(M1):"+m1);
        String A="",copy="";
		for (int i = 0; i < c; i++) {
			A = A + "0";
		} 
        System.out.println("\nA:"+A);
        char lsb= m.charAt(c-1);
        System.out.println("\nQ:"+m);
        int count =c;
        String carry = "0";
        System.out.println("\nCarry:"+carry);
        while(count>0){
            System.out.println("\n");
            System.out.println("Count:"+count);
        if(lsb=='1'){
            String[] result = binaryadd(A,m1);
            copy=result[1]+result[0];
                A=copy.substring(1);
                carry=result[1];
        }
            m = A.charAt(A.length()-1) + m.substring(0, m.length() - 1);
            A = carry + A.substring(0, A.length() - 1);
             System.out.println("\nC:"+carry);
            System.out.println("\nA:"+A);
            System.out.println("\nQ:"+m);
            lsb=m.charAt(m.length()-1);
            count=count-1;
            carry="0";
    }
    String mul = A+m;
    System.out.println("\nBinary output:"+mul);
    Long dec = binarytodec(mul);
    System.out.println("\nDecimal:"+dec);
    }
    public static String binary(int n) {
        return Integer.toBinaryString(n);
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
    public static String[] binaryadd(String s1, String s2) {
    String[] strings = new String[2];
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

	strings[0] = res;
    strings[1] = carry;
    return strings;

	}
}
