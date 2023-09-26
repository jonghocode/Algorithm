import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int r, c, answer;
    static char[][] alpha = new char[21][21];
    static int[] zx = {-1, 1, 0, 0};
    static int[] zy = {0, 0, -1, 1};
    static int[] chk = new int [200];
    static int[][] chk2 = new int[21][21];
    public static void dfs(int x, int y, int d){
        if(answer < d){
            answer = d;
        }

        for(int i=0; i<4; i++){
            int nx = x + zx[i];
            int ny = y + zy[i];
            if(nx>=0 && nx<r && ny>=0 && ny<c && chk2[nx][ny] == 0
            && chk[alpha[nx][ny]-'A'+1] == 0){
                chk[alpha[nx][ny]-'A'+1] = 1;
                chk2[nx][ny] = 1;
                dfs(nx, ny, d+1);
                chk[alpha[nx][ny]-'A'+1] = 0;
                chk2[nx][ny] = 0;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        r = sc.nextInt(); c = sc.nextInt();

        for(int i=0; i<r; i++){
            alpha[i] = sc.next().toCharArray();
        }
        chk[alpha[0][0]-'A'+1]=1;
        chk2[0][0] = 1;
        dfs(0,0, 1);
        System.out.println(answer);
    }
}