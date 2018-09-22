# -*- coding: utf-8 -*-
import os
import sys

import re
import unicodedata
import random
import numpy as np

INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐ"
INTAB = [ch.encode('utf8') for ch in unicode(INTAB, 'utf8')]


OUTTAB = "a" * 17 + "o" * 17 + "e" * 11 + "u" * 11 + "i" * 5 + "y" * 5 + "d" + \
         "A" * 17 + "O" * 17 + "E" * 11 + "U" * 11 + "I" * 5 + "Y" * 5 + "D"

r = re.compile("|".join(INTAB))
replaces_dict = dict(zip(INTAB, OUTTAB))


def no_accent_vietnamese(utf8_str):
    return r.sub(lambda m: replaces_dict[m.group(0)], utf8_str)

def list_image(dir, kk=20):
	images = [img for img in os.listdir(dir) if (img[-4:] == '.png' or img[-4:] == '.jpg')]
	#random.seed(9001)
	if len(images) >= kk:
		return random.sample(images, k=kk)
	else:
		return np.random.choice(images, kk)

names = [
"Vũ Khắc Dương",
"Phạm Xuân Thành",
"Phạm Văn Lân",
"Nguyễn Tiến Nam",
"Trịnh Tiến Thành",
"Nguyễn Hoàng Sơn",
"Lê Mạnh Đức",
'Nguyễn Hoàng Anh',
'Lê Thành Nhân',
'Đặng Anh Khoa',
'Nguyễn Đức Thành',
'Nhâm Duy Khương',
'Nguyễn Thế Vinh',
'Trần Công Thành',
'kim Trung Hiếu',
'Nguyễn Trung Kiên',
'Trịnh Tuấn Tú',
'Trịnh Lê Gia Tuyên',
'Ngô Đức Thắng',
'Trương Đức Dũng',
'Nguyễn Tiến Dũng',
'Đào Đức Nguyên',
'Nguyễn Hồng Sơn',
'Hoàng Nguyên Khánh',
'Đỗ Hữu Đức',
'Nguyễn Hoàng Hải',
'Đỗ Thu Hà',
'Tạ Thị Thanh Lâm',
'L.D.Thushanga Jayasinghe',
'Nguyễn Thành Long',
'Nguyễn Quang Vinh',
'Phan Đại Dương',
'Phạm Ngọc Sơn',
'Nguyễn Huy Hoàng',
'Lê NGuyễn Dũng',
'Phùng Lâm Ngọc Bội'
]

sdt = [
1676889215,
1626633332,
1655641010,
1642179494,
948349242,
1687872468,
962546705,
975049346,
1672049934,
936348433,
962911998,
962941498,
868756103,
965554698,
1272261098,
983338466,
913293179,
1239809686,
1663092190,
1662880198,
966678498,
1648023999,
1643737489,
1637393456,
1632154111,
961180109,
988615776,
1659932288,
1663125767,
1648965522,
941177055,
1239646851,
1644232828,
981512747,
1652352525,
971458399
]

root_folder = sys.argv[1]
start_num = sys.argv[2]

for i,n in enumerate(names):
	names[i] = no_accent_vietnamese(names[i])

with open("meta_data_face.txt", 'w') as data_file:
	data_file.write(str(len(names)) + '\n')
	for i,n in enumerate(names):
		data_file.write(names[i]+'\t' + str(sdt[i]) +  '\n')
		data_file.write(str(sdt[i]) + '\n')
		data_file.write(str(30) + '\n')
		fd_class = os.path.join(root_folder,start_num+'_VS')
		imgs = list_image(fd_class, 30)

		start_num = str(int(start_num) + 1)

		for im in imgs:
			data_file.write(os.path.join(fd_class,im) + '\n')

print (names)
