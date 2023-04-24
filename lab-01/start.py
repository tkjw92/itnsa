from os import system as st

st('echo "auto lo" > /etc/network/interfaces')
st('echo "iface lo inet loopback" >> /etc/network/interfaces')

st('systemctl restart networking')
st('ip addr flush enp0s3')
st('ip addr flush enp0s8')

st('echo "Lab-01 berhasil disiapkan, selamat mengerjakan\n\n"')
