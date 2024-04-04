import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;

public class Main {
    public static void main(String[] args)  {
        int key = 0, now = 0, watingTime = 0;

        Object[] list = new Object[4];
        list[0] = event("A", 20, 5);
        list[1] = event("B", 22, 4);
        list[2] = event("C", 23, 2);
        list[3] = event("D", 30, 3);

        Queue<Object> queue = new ArrayDeque<>();
        queue.add(list[0]);
        while (!queue.isEmpty()) {
            Map<String, Object> temp = (Map<String, Object>)queue.remove();
            String who = temp.get("customer").toString();
            int st = Integer.parseInt(temp.get("start").toString());
            int time = Integer.parseInt(temp.get("time").toString());

            if (now >= st && key < 3) { // 도착 시간이 되었으니 큐에 넣기
                queue.add(list[++key]);
            }
            else if(now < st){
                queue.add(list[key]);
            }

            if (now >= st) {
                System.out.println("손님 : " + who + ", 도착시간 : " + st + ", " +
                        "서비스 시작시간 : " + now + ", 서비스 완료 시간 : " + (now + time));
                watingTime += now - st;
                now += time;
            } else {
                now ++;
            }
        }

        System.out.println("평균 대기 시간 : " + watingTime / 4);
    }

    static Map<String, Object> event(String customer, int endtime, int time) {
        Map<String, Object> map = new HashMap<>();
        map.put("customer", customer);
        map.put("start", endtime);
        map.put("time", time);
        return map;
    }
}