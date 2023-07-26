import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[] arr = new int [12];
    static int ma = -1000000010;
    static int mi = 1000000000;
    static int n;
    public static void dfs(int x, int y, int o, int p, int sum, int idx){
        if(idx == n){
            if(sum > ma)ma = sum;
            if(sum < mi)mi = sum;
            return;
        }

        if(x>=1){
            dfs(x-1, y, o, p, sum+arr[idx], idx+1);
        }
        if(y>=1){
            dfs(x, y-1, o, p, sum-arr[idx], idx+1);
        }
        if(o>=1){
            dfs(x, y, o-1, p, sum*arr[idx], idx+1);
        }
        if(p>=1){
            dfs(x, y, o, p-1, sum/arr[idx], idx+1);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, c, d;
        n = sc.nextInt();
        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        a = sc.nextInt(); b = sc.nextInt();
        c = sc.nextInt(); d = sc.nextInt();

        dfs(a, b, c, d, arr[0], 1);
        System.out.println(ma);
        System.out.println(mi);
    }
}