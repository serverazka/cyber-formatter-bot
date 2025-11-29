from datetime import datetime

def format_data_as_table(data):
    """Format data sebagai table yang rapi dengan alignment"""
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

def generate_formatted_text(data, theme="forensic"):
    """Generate formatted text berdasarkan theme"""
    from templates.forensic import forensic_template
    from templates.modern import modern_template
    from templates.cyberpunk import cyberpunk_template
    from templates.military import military_template
    
    if theme == "modern":
        return modern_template(data)
    elif theme == "cyberpunk":
        return cyberpunk_template(data)
    elif theme == "military":
        return military_template(data)
    elif theme == "dark":
        return military_template(data)
    elif theme == "classified":
        return military_template(data)
    else:
        return forensic_template(data)

def split_long_message(text, max_length=4000):
    """Split message jika terlalu panjang"""
    if len(text) <= max_length:
        return [text]
    
    parts = []
    while text:
        if len(text) <= max_length:
            parts.append(text)
            break
        else:
            split_pos = text.rfind('\n', 0, max_length)
            if split_pos == -1:
                split_pos = max_length
            parts.append(text[:split_pos])
            text = text[split_pos:].strip()
    
    return parts