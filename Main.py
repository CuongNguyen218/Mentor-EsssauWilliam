import Node
import InitialTopo
import MENTOR
import EsauWilliam
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max', type=int, default=1000, help='Thong so mat phang MAX x MAX')
    parser.add_argument('--num_node', type=int, default=90, help='So nut trong mang')
    parser.add_argument('--radius', type=float, default=0.3, help='Ty le de tinh ban kinh trong Mentor')
    parser.add_argument('--C', type=int, default=10, help='Dung luong 1 lien ket')
    parser.add_argument('--w', type=int, default=2, help='Trong so luu luong chuan hoa de xet nut backbone của MENTOR')
    parser.add_argument('--w_ew', type=int, default=10, help='Trong so nguong cua cac nhom trong cay truy nhap của EW')
    parser.add_argument('--limit_mentor', type=int, default=0,
                        help='Gioi han cua thuat toan mentor')
    parser.add_argument('--limit_ew', type=int, default=4,
                        help='Gioi han so nut trong cay cua EW')
    parser.add_argument('--debug', type=bool, default=False,
                        help='Che do Debug')

    return parser.parse_args()


def main():
    args = parse_args()
    ListPosition = InitialTopo.Global_Init_Topo(args.max, args.num_node, args.debug)
    #ListPosition = InitialTopo.Global_Init_Topo_Fix_Position(MAX,NumNode,False)
    # False/ True: Nếu chọn True, toàn bộ các bước trong tạo topology mạng sẽ được giám sát và hiển thị

    ListMentor = MENTOR.MenTor(ListPosition, args.max, args.C, args.w, args.radius, args.limit_mentor, args.debug)
    # 5: Là số giới hạn nút đầu cuối của thuật toán MENTOR.
    # Khi một nút Backbone tìm thấy số lượng nút đầu cuối đạt của một mạng truy nhập tới giới hạn. Nó ngừng việc quét tìm nút đầu cuối. Nếu cài đặt giá trị này bằng 0 thì xem như không có giới hạn số lượng nút đầu cuối.
    # False/ True: Bật tắt giám sát thuật toán

    ListFinish = EsauWilliam.Esau_William(ListMentor, args.w_ew, args, args.limit_ew, args.debug)
    # False/ True: Bật tắt giám sát thuật toán
    # 5: Giới hạn số nút trên cây truy nhập. Nếu đặt bằng 0 thì không giới hạn.

    Node.printList2D(ListFinish)
    Node.matplot_total(ListFinish, args.max)
    Node.plt.show()

if __name__ == '__main__':
    main()
