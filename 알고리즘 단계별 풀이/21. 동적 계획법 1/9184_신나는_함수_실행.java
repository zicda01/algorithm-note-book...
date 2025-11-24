import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while(true) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();
            if (a == -1 && b == -1 && c == -1) {
                break;
            }
            int result = w(a, b, c);
            System.out.println("w(" + a + ", " + b + ", " + c + ")" + " = " + result);
        }
    }
    public static int w(int a, int b, int c) {
        if(a <= 0 || b <= 0 || c <= 0) {
            return 1;
        } else if(a > 20 || b > 20 || c > 20) {
            return w(20, 20, 20);
        } else if(volume[a][b][c] != 0) {
            return volume[a][b][c];
        }

        int result;
        if (a < b && b < c ) {
            result =  w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
        } else {
            result = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1) ;
        }
        volume[a][b][c] = result ;
        return result ;
    }
    public static int[][][] volume = new int[21][21][21];
}