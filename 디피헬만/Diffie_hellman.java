package info_sec;

import java.util.*;

public class Diffie_hellman {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int p = selectP(1024);
		int g = findGenerator(p);
		
		System.out.println("Enter Alice's Key : ");
		int a = sc.nextInt();	
		System.out.println("Enter Bob's Key : ");
		int b = sc.nextInt();
		
		int x = power(g,a,p);
		int y = power(g,b,p);
		
		int ka = power(y,a,p);
		int kb = power(x,b,p);
		
		if (ka == kb) {
			System.out.println("Alice & Bob's Shared Secret Key : " + ka);
		}
		
		sc.close();
	}
	static boolean isPrime(int n)
    {
        if (n <= 1)
        {
            return false;
        }
        if (n <= 3)
        {
            return true;
        }

        if (n % 2 == 0 || n % 3 == 0)
        {
            return false;
        }
 
        for (int i = 5; i * i <= n; i = i + 6)
        {
            if (n % i == 0 || n % (i + 2) == 0)
            {
                return false;
            }
        }
        return true;
    }
	static int selectP(int n) {
		for (int i=n; i > 0; i--) {
			if (isPrime(i) == true) {
				return i;
			}
		}
		return n;
	}
	static int power(int x, int y, int p)
    {
        int res = 1;   
        x = x % p; 
        while (y > 0)
        {
            if (y % 2 == 1)
            {
                res = (res * x) % p;
            }
            y = y >> 1; 
            x = (x * x) % p;
        }
        return res;
    }
    static void findPrimefactors(HashSet<Integer> s, int n)
    {
        while (n % 2 == 0)
        {
            s.add(2);
            n = n / 2;
        }
        for (int i = 3; i <= Math.sqrt(n); i = i + 2)
        {
            while (n % i == 0)
            {
                s.add(i);
                n = n / i;
            }
        }
        if (n > 2)
        {
            s.add(n);
        }
    }
    static int findGenerator(int n)
    {
        HashSet<Integer> s = new HashSet<Integer>();
        if (isPrime(n) == false)
        {
            return -1;
        }
        int phi = n - 1;
        findPrimefactors(s, phi);
        for (int r = phi ; r >= 0; r--)
        {
            boolean flag = false;
            for (Integer a : s)
            {
                if (power(r, phi / (a), n) == 1)
                {
                    flag = true;
                    break;
                }
            }

            if (flag == false)
            {
                return r;
            }
        }
        return -1;
    }
}
