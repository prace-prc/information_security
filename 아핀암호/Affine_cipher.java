package info_sec;

import java.util.Scanner;

public class Affine_cipher {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Input Message : ");
		String message = sc.nextLine();
		System.out.println("Input : " + message);
		System.out.println("Encrypted Msg : " + encryptMsg(message.toCharArray()));
		System.out.println("Decrypted Msg : " + decryptMsg(encryptMsg(message.toCharArray())));
		sc.close();
	}
	
	public static String encryptMsg(char[] Msg) {
		String txt = "";
		int key1 = 17;
		int key2 = 20;
		for (int i=0; i < Msg.length; i++) { 
			if (Msg[i] != ' ') {
			txt = txt + (char) ((((key1 * Msg[i] - 65) + key2) % 26) + 65);}
			else {
				txt += Msg[i];
			}
		}
		
		return txt;
	}
	
	public static String decryptMsg(String txt) {
		String Msg = "";
		int key1 = 17;
		int key2 = 20;
		int key1_inverse = 0;
		int flag =0;
		
		for (int i = 0; i < 26; i++) {
			flag = (key1 * i) % 26;
			if (flag == 1) {
				key1_inverse = i;
			}
		}
		
		for (int i = 0; i < txt.length(); i++) {
			if(txt.charAt(i) != ' ') {
				Msg = Msg + (char) (((key1_inverse * ((txt.charAt(i) + 65 - key2)) % 26)) + 65);
			}
			else {
				Msg += txt.charAt(i);
			}
		}
		
		return Msg;
	}
}
