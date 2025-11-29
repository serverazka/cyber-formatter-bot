from datetime import datetime

def format_data_as_table(data):
    """Copy function dari formatter.py"""
    table = ""
    
    field_names = {
        'nik': 'NIK',
        'nama': 'Nama Lengkap', 
        'alamat': 'Alamat',
        'kabupaten': 'Kabupaten',
        'kecamatan': 'Kecamatan', 
        'kelurahan': 'Kelurahan',
        'jenis_kelamin': 'Jenis Kelamin',
        'golongan_darah': 'Gol. Darah',
        'agama': 'Agama',
        'pekerjaan': 'Pekerjaan',
        'imei': 'IMEI',
        'serial': 'Serial Number',
        'ip': 'IP Address',
        'device': 'Device',
        'status': 'Status'
    }
    
    max_key_length = 0
    for key in data.keys():
        display_name = field_names.get(key, key.replace('_', ' ').title())
        max_key_length = max(max_key_length, len(display_name))
    
    for key, value in data.items():
        display_name = field_names.get(key, key.replace('_', ' ').title())
        padding = max_key_length - len(display_name)
        table += f"{display_name}{' ' * padding} : {value}\n"
    
    return table

def cyberpunk_template(data):
    """Template cyberpunk style"""
    table = format_data_as_table(data)
    
    return f"""
╔═══════════════════════════════╗
║    ＣＹＢＥＲ-ＦＯＲＥＮＳＩＣ-Ｖ２.⓿    ║
╚═══════════════════════════════╝

 neon > TIMESTAMP: {datetime.now().strftime("%Y-%m-%d %H:%M")}
 glow > CASE_ID: CP-{int(datetime.now().timestamp())}
 matrix > STATUS: VERIFIED

{table}

⚠️  DATA_ANOMALY_DETECTED: 0%
🔒 ENCRYPTION_LEVEL: AES-256
⚡ SYSTEM_STATUS: NOMINAL
"""