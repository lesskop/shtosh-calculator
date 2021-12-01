from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01r\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 height=\x224\
8px\x22 viewBox=\x220 \
0 24 24\x22 width=\x22\
48px\x22 fill=\x22#FFF\
FFF\x22><path d=\x22M0\
 0h24v24H0z\x22 fil\
l=\x22none\x22/><path \
d=\x22M22 3H7c-.69 \
0-1.23.35-1.59.8\
8L0 12l5.41 8.11\
c.36.53.9.89 1.5\
9.89h15c1.1 0 2-\
.9 2-2V5c0-1.1-.\
9-2-2-2zm-3 12.5\
9L17.59 17 14 13\
.41 10.41 17 9 1\
5.59 12.59 12 9 \
8.41 10.41 7 14 \
10.59 17.59 7 19\
 8.41 15.41 12 1\
9 15.59z\x22/></svg\
>\
\x00\x00\x01\xea\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 enable-ba\
ckground=\x22new 0 \
0 20 20\x22 height=\
\x2248px\x22 viewBox=\x22\
0 0 20 20\x22 width\
=\x2248px\x22 fill=\x22#0\
00000\x22><g><rect \
fill=\x22none\x22 heig\
ht=\x2220\x22 width=\x222\
0\x22/></g><g><g><p\
ath d=\x22M16,4H4v1\
2h12V4z M6,7.27h\
3v1H6V7.27z M10,\
12.5H8.5V14h-1v-\
1.5H6v-1h1.5V10h\
1v1.5H10V12.5z M\
14,13.25h-3v-1h3\
V13.25z M14,11.7\
5h-3v-1h3V11.75z\
 M14.27,8.83l-0.\
71,0.71L12.5,8.4\
7l-1.06,1.06l-0.\
71-0.71l1.06-1.0\
6l-1.06-1.06L11.\
44,6l1.06,1.06 L\
13.56,6l0.71,0.7\
1l-1.06,1.06L14.\
27,8.83z\x22/></g><\
/g></svg>\
"

qt_resource_name = b"\
\x00\x05\
\x00o\xa6S\
\x00i\
\x00c\x00o\x00n\x00s\
\x00\x0d\
\x07d\x0f\xa7\
\x00b\
\x00a\x00c\x00k\x00s\x00p\x00a\x00c\x00e\x00.\x00s\x00v\x00g\
\x00\x0e\
\x0b0\xc5\xa7\
\x00c\
\x00a\x00l\x00c\x00u\x00l\x00a\x00t\x00o\x00r\x00.\x00s\x00v\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x10\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01}v\x96\x94\xeb\
\x00\x00\x000\x00\x00\x00\x00\x00\x01\x00\x00\x01v\
\x00\x00\x01}v\x96\xb7]\
"


def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)


def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)


qInitResources()
