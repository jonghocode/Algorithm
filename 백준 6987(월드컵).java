import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[][] a = new int[8][8];
    static int sw = 0;
    public static void search(int x, int y){
        if(sw == 1)return;
        if(y==7){
            x++; y=x+1;
        }
        if(x==6){
            sw = 1;
            return;
        }
        if(a[x][1] >= 1 && a[y][3] >= 1){
            a[x][1]--; a[y][3]--;
            search(x, y+1);
            a[x][1]++; a[y][3]++;
        }
        if(a[x][2] >= 1 && a[y][2] >= 1){
            a[x][2]--; a[y][2]--;
            search(x, y+1);
            a[x][2]++; a[y][2]++;
        }
        if(a[x][3] >= 1 && a[y][1] >= 1){
            a[x][3]--; a[y][1]--;
            search(x, y+1);
            a[x][3]++; a[y][1]++;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for(int p=1; p<=4; p++){
            int sw2 = 0;
            for(int i=1; i<=6; i++){
                int sum = 0;
                for(int j=1; j<=3; j++){
                    a[i][j] = sc.nextInt();
                    sum+=a[i][j];
                }
                if(sum > 5)sw2 = 1;
            }
            sw = 0;
            if(sw2 == 0)search(1,2);
            System.out.print(sw+" ");
        }
    }
}