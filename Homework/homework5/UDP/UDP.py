import struct
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def check(data):
    sum = 0
    for i in range(0, len(data), 16):
        val = int(data[i:i + 16], 2)
        sum = sum + val
        sum = sum & 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)

    if sum > 65535:
        sum = (sum >> 16) + (sum & 0xffff)

    return 65535-sum


a = '011001100110000001010101010101011000111100001100'
ip_check = check(a)
print('ip_check:', bin(ip_check))



#
# def check(data):
#     sum = 0
#     for i in range(0, len(data), 4):
#         val = int(data[i:i + 4], 16)
#         sum = sum + val
#         sum = sum & 0xffffffff
#
#     sum = (sum >> 16) + (sum & 0xffff)
#     if sum > 65535:
#         sum = (sum >> 16) + (sum & 0xffff)
#
#     return 65535 - sum
#
#
# initial_text = ""
#
#
# def submit(text):
#     text = text_box1.text + text_box2.text + text_box3.text
#     udp_check = check(text)
#     axbox4 = plt.axes([0.2, 0.4, 0.5, 0.075])
#     text_box4 = TextBox(axbox4, 'udp_check:', initial=hex(udp_check))
#     plt.draw()
#
#
# axbox1 = plt.axes([0.2, 0.8, 0.5, 0.075])
# text_box1 = TextBox(axbox1, 'A 16 bits:', initial=initial_text)
#
# axbox2 = plt.axes([0.2, 0.7, 0.5, 0.075])
# text_box2 = TextBox(axbox2, 'A 16 bits:', initial=initial_text)
#
# axbox3 = plt.axes([0.2, 0.6, 0.5, 0.075])
# text_box3 = TextBox(axbox3, 'A 16 bits:', initial=initial_text)
#
# text_box3.on_submit(submit)
#
# plt.show()