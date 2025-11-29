import re
from utils.validator import clean_value

def parse_text_input(text):
    """Smart parser untuk berbagai format input"""
    data = {}
    
    # Bersihkan emoticon dan karakter khusus
    clean_text = re.sub(r'[✅🆔👤📍🏛️🏘️🏠⚧️🩸🕌💼➡️🔍📱🖥️💻📶📡🌐]', '', text)
    
    # Pattern matching
    patterns = {
        'nik': r'(?:^|\n)NIK\s*:?\s*(\d{16})(?=\n|$)',
        'nama': r'(?:^|\n)(?:Nama\s*(?:Lengkap)?)\s*:?\s*([^\n:]+)(?=\n|$)',
        'alamat': r'(?:^|\n)Alamat\s*:?\s*([^\n]+)(?=\n|$)',
        'kabupaten': r'(?:^|\n)Kabupaten\s*:?\s*([^\n]+)(?=\n|$)',
        'kecamatan': r'(?:^|\n)Kecamatan\s*:?\s*([^\n]+)(?=\n|$)',
        'kelurahan': r'(?:^|\n)Kelurahan\s*:?\s*([^\n]+)(?=\n|$)',
        'jenis_kelamin': r'(?:^|\n)(?:Jenis\s+Kelamin|JK|Gender)\s*:?\s*([^\n]+)(?=\n|$)',
        'golongan_darah': r'(?:^|\n)(?:Golongan\s+Darah|Goldar)\s*:?\s*([^\n]+)(?=\n|$)',
        'agama': r'(?:^|\n)Agama\s*:?\s*([^\n]+)(?=\n|$)',
        'pekerjaan': r'(?:^|\n)Pekerjaan\s*:?\s*([^\n]+)(?=\n|$)',
        'imei': r'(?:^|\n)IMEI\s*:?\s*([^\n]+)(?=\n|$)',
        'serial': r'(?:^|\n)(?:Serial|Serial\s+Number)\s*:?\s*([^\n]+)(?=\n|$)',
        'ip': r'(?:^|\n)(?:IP|IP\s+Address)\s*:?\s*([^\n]+)(?=\n|$)',
    }
    
    for field, pattern in patterns.items():
        match = re.search(pattern, clean_text, re.IGNORECASE)
        if match:
            value = clean_value(match.group(1))
            data[field] = value
    
    # Fallback parsing
    if not data:
        lines = clean_text.split('\n')
        current_key = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if ':' in line:
                key_part, value_part = line.split(':', 1)
                key = key_part.strip().lower().replace(' ', '_')
                value = clean_value(value_part)
                
                if key and value:
                    data[key] = value
                    current_key = key
            elif current_key and line:
                data[current_key] += ' ' + clean_value(line)
    
    return data

def detect_template_type(data):
    """Deteksi template berdasarkan data yang ada"""
    if 'nik' in data:
        return 'forensic'
    elif 'imei' in data or 'serial' in data:
        return 'device'
    elif 'ip' in data:
        return 'network'
    else:
        return 'general'