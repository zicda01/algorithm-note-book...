import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int length = N;
        if(N <= 2) {
            length = 2;
        }
        int[] array = new int[length];
        int mod = 15746;
        array[0] = 1;
        array[1] = 2;
        for(int i = 2; i < length; i++){
            array[i] = (array[i - 1] + array[i - 2]) % mod;
        }

        int result;

        result = array[N - 1];
        System.out.println(result);
        }
}