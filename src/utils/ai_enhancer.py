import re

def detect_gender_from_nik(nik):
    """Deteksi gender dari NIK (digit ke-14)"""
    if not nik or len(nik) < 14:
        return None
    
    digit_14 = int(nik[13])
    return "PEREMPUAN" if digit_14 % 2 == 0 else "LAKI-LAKI"

def detect_gender_from_name(name):
    """Deteksi gender dari nama (simple version)"""
    female_indicators = ['sari', 'dewi', 'putri', 'rani', 'inta', 'ika']
    male_indicators = ['adi', 'bud', 'wan', 'ton', 'sus', 'riz']
    
    name_lower = name.lower()
    
    for indicator in female_indicators:
        if indicator in name_lower:
            return "PEREMPUAN"
    
    for indicator in male_indicators:
        if indicator in name_lower:
            return "LAKI-LAKI"
    
    return None

def enhance_location(address):
    """Enhance alamat dengan format yang lebih baik"""
    if not address:
        return address
    
    # Simple location enhancement
    enhancements = {
        'dsn': 'DSN',
        'ds': 'DS',
        'rt': 'RT',
        'rw': 'RW',
        'jl': 'JL',
        'jr': 'JR',
        'gg': 'GG'
    }
    
    enhanced = address
    for short, full in enhancements.items():
        enhanced = re.sub(r'\b' + short + r'\b', full, enhanced, flags=re.IGNORECASE)
    
    return enhanced

def capitalize_name(name):
    """Kapitalisasi nama dengan benar"""
    if not name:
        return name
    
    # List kata yang tidak perlu dikapitalisasi penuh
    lowercase_words = ['bin', 'binti', 'de', 'van', 'der']
    
    words = name.split()
    capitalized_words = []
    
    for word in words:
        if word.lower() in lowercase_words:
            capitalized_words.append(word.lower())
        else:
            capitalized_words.append(word.capitalize())
    
    return ' '.join(capitalized_words)

def ai_enhance_data(data):
    """Main AI enhancement function"""
    enhanced_data = data.copy()
    
    # Gender detection
    if 'nik' in enhanced_data and 'jenis_kelamin' not in enhanced_data:
        gender = detect_gender_from_nik(enhanced_data['nik'])
        if gender:
            enhanced_data['jenis_kelamin'] = gender
    
    if 'nama' in enhanced_data and 'jenis_kelamin' not in enhanced_data:
        gender = detect_gender_from_name(enhanced_data['nama'])
        if gender:
            enhanced_data['jenis_kelamin'] = gender
    
    # Name capitalization
    if 'nama' in enhanced_data:
        enhanced_data['nama'] = capitalize_name(enhanced_data['nama'])
    
    # Location enhancement
    if 'alamat' in enhanced_data:
        enhanced_data['alamat'] = enhance_location(enhanced_data['alamat'])
    
    return enhanced_data