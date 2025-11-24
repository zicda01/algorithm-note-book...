import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        fibonacci_recurrsion(N);
        fibonacci_dp(N);
        String result = String.valueOf(counter_recursion) + " " + String.valueOf(counter_dp);
        System.out.println(result);
    }

    public static int fibonacci_recurrsion(int n) {
        if (n == 1 || n == 2) {
            counter_recursion += 1;
            return 1;
        }
        return fibonacci_recurrsion(n - 1) + fibonacci_recurrsion(n - 2);
    }

    public static int fibonacci_dp(int n) {
        int[] fibo_array = new int[n];
        fibo_array[0] = 1;
        fibo_array[1] = 1;
        for (int i = 2; i < n; i++) {
            fibo_array[i] = fibo_array[i - 1] + fibo_array[i - 2];
            counter_dp += 1;
        }
        return fibo_array[n - 1];
    }

    public static int counter_recursion = 0;
    public static int counter_dp = 0;
}