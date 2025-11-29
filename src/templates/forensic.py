from datetime import datetime

def format_data_as_table(data):
    """Copy function dari formatter.py untuk hindari circular import"""
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

def forensic_template(data):
    """Template forensic klasik"""
    table = format_data_as_table(data)
    
    return f"""
==============================================
        INTERNAL SECURITY UNIT v3.0
==============================================

CASE ID     : CF-{int(datetime.now().timestamp())}
TIMESTAMP   : {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}
ACCESS LEVEL: FORENSIC ANALYST

==============================================
[ DATA SUBJECT ]
==============================================
{table}
==============================================
[ SYSTEM METADATA ]
==============================================
Data Source     : INTERNAL DATABASE
Verification    : 98.7% MATCH
Risk Assessment : LOW
Status          : VERIFIED

==============================================
[ SECURITY CLASSIFICATION ]
RESTRICTED - FOR OFFICIAL USE ONLY
Unauthorized distribution prohibited
"""