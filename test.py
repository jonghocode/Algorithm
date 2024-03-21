// 이름, 전화번호, 이메일, 주소를 저장하는 주소록 작성
// 1) 주소록 Node 클래스 정의(이름, 전화번호, 이메일, 주소 필드)
// 2) 자바 linkedlist 클래스 활용
// 3) 데이터 추가, 삭제, 조회 기능 추가
// 4 ) 전체 데이터 양방향 출력
class Data {
    private String name;
    private String phone;
    private String email;
    private String address;

    public Data(String name, String phone, String email, String address) {
        this.name = name;
        this.phone = phone;
        this.email = email;
        this.address = address;
    }

    public String getName() {
        return name;
    }

    public String getPhone() {
        return phone;
    }

    public String getEmail() {
        return email;
    }

    public String getAddress() {
        return address;
    }
}
class Node {
    Data data;
    Node next;

    public Node(Data data) {
        this.data = data;
        this.next = null;
    }

    public Node(Data data, Node next) {
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    private Node head;

    public LinkedList() {
        this.head = null;
    }

    void insert(Data data) {
        Node node = new Node(data);
        if (head == null) {
            head = node;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = node;
        }
    }

    void delete(String phone) {
        if (head == null) {
            System.out.println("연락처가 비어있습니다.");
            return;
        }

        // 삭제할 노드가 첫 번째 노드인 경우
        if (head.data.getPhone().equals(phone)) {
            head = head.next;
            return;
        }

        Node prev = head;
        Node current = head.next;

        while (current != null && !current.data.getPhone().equals(phone)) {
            prev = current;
            current = current.next;
        }

        if (current == null) {
            System.out.println("해당 연락처가 존재하지 않습니다.");
            return;
        }

        prev.next = current.next;
    }



    void select() {
        if (head == null) {
            System.out.println("연락처가 비어있습니다.");
        } else {
            Node current = head;
            while (current.next != null) {
                System.out.println("{ 이름 : " + current.data.getName() + " / 전화번호 : " + current.data.getPhone()
                + " / 이메일 : " + current.data.getEmail() + " / 주소 : " + current.data.getAddress() + " }");
                current = current.next;
            }
            System.out.println("{ 이름 : " + current.data.getName() + " / 전화번호 : " + current.data.getPhone()
                    + " / 이메일 : " + current.data.getEmail() + " / 주소 : " + current.data.getAddress() + " }");
        }
    }
}
public class Main {
    public static void main(String[] args)  {
        LinkedList list = new LinkedList();
        Data data1 = new Data("홍길동", "010-1234-5678", "abc@naver.com", "대구");
        Data data2 = new Data("하니", "010-4455-7788", "abcd@naver.com", "영진");
        Data data3 = new Data("뉴진스", "010-8899-5678", "abce@naver.com", "전문");
        Data data4 = new Data("안녕", "010-6655-5678", "abk@naver.com", "대학");
        list.insert(data1);
        list.insert(data2);
        list.insert(data3);
        list.insert(data4);
        list.select();
        System.out.println("삭제 후");
        list.delete("010-1234-5678");
        list.select();
    }
}
