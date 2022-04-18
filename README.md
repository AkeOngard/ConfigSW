# ConfigSW
Install library from file requirement by using 

pip install -r requirments.txt

ฟังก์ชั่นของ Netmiko เบื้องต้น
ConnectHandler() = สร้าง object ของ connection/session
enable() = เข้าสู่ privilege mode
config_mode() = เข้าสู่ configuration mode
exit_enable_mode() = ออกจาก privilege mode
exit_config_mode() = ออกจาก configuration mode
send_command() = ส่ง command และ return ค่า output
send_config_set() = ส่ง command เป็น list และ return ค่า output
disconnect() = ตัด SSH connection
