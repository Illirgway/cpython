""" Python Character Mapping Codec generated from 'MAPPINGS/VENDORS/MICSFT/EBCDIC/CP500.TXT' with gencodec.py.

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):

        return codecs.charmap_encode(input,errors,encoding_map)

    def decode(self,input,errors='strict'):

        return codecs.charmap_decode(input,errors,decoding_table)
    
class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():

    return (Codec().encode,Codec().decode,StreamReader,StreamWriter)


### Decoding Table

decoding_table = (
    u'\x00'	#  0x00 -> NULL
    u'\x01'	#  0x01 -> START OF HEADING
    u'\x02'	#  0x02 -> START OF TEXT
    u'\x03'	#  0x03 -> END OF TEXT
    u'\x9c'	#  0x04 -> CONTROL
    u'\t'	#  0x05 -> HORIZONTAL TABULATION
    u'\x86'	#  0x06 -> CONTROL
    u'\x7f'	#  0x07 -> DELETE
    u'\x97'	#  0x08 -> CONTROL
    u'\x8d'	#  0x09 -> CONTROL
    u'\x8e'	#  0x0a -> CONTROL
    u'\x0b'	#  0x0b -> VERTICAL TABULATION
    u'\x0c'	#  0x0c -> FORM FEED
    u'\r'	#  0x0d -> CARRIAGE RETURN
    u'\x0e'	#  0x0e -> SHIFT OUT
    u'\x0f'	#  0x0f -> SHIFT IN
    u'\x10'	#  0x10 -> DATA LINK ESCAPE
    u'\x11'	#  0x11 -> DEVICE CONTROL ONE
    u'\x12'	#  0x12 -> DEVICE CONTROL TWO
    u'\x13'	#  0x13 -> DEVICE CONTROL THREE
    u'\x9d'	#  0x14 -> CONTROL
    u'\x85'	#  0x15 -> CONTROL
    u'\x08'	#  0x16 -> BACKSPACE
    u'\x87'	#  0x17 -> CONTROL
    u'\x18'	#  0x18 -> CANCEL
    u'\x19'	#  0x19 -> END OF MEDIUM
    u'\x92'	#  0x1a -> CONTROL
    u'\x8f'	#  0x1b -> CONTROL
    u'\x1c'	#  0x1c -> FILE SEPARATOR
    u'\x1d'	#  0x1d -> GROUP SEPARATOR
    u'\x1e'	#  0x1e -> RECORD SEPARATOR
    u'\x1f'	#  0x1f -> UNIT SEPARATOR
    u'\x80'	#  0x20 -> CONTROL
    u'\x81'	#  0x21 -> CONTROL
    u'\x82'	#  0x22 -> CONTROL
    u'\x83'	#  0x23 -> CONTROL
    u'\x84'	#  0x24 -> CONTROL
    u'\n'	#  0x25 -> LINE FEED
    u'\x17'	#  0x26 -> END OF TRANSMISSION BLOCK
    u'\x1b'	#  0x27 -> ESCAPE
    u'\x88'	#  0x28 -> CONTROL
    u'\x89'	#  0x29 -> CONTROL
    u'\x8a'	#  0x2a -> CONTROL
    u'\x8b'	#  0x2b -> CONTROL
    u'\x8c'	#  0x2c -> CONTROL
    u'\x05'	#  0x2d -> ENQUIRY
    u'\x06'	#  0x2e -> ACKNOWLEDGE
    u'\x07'	#  0x2f -> BELL
    u'\x90'	#  0x30 -> CONTROL
    u'\x91'	#  0x31 -> CONTROL
    u'\x16'	#  0x32 -> SYNCHRONOUS IDLE
    u'\x93'	#  0x33 -> CONTROL
    u'\x94'	#  0x34 -> CONTROL
    u'\x95'	#  0x35 -> CONTROL
    u'\x96'	#  0x36 -> CONTROL
    u'\x04'	#  0x37 -> END OF TRANSMISSION
    u'\x98'	#  0x38 -> CONTROL
    u'\x99'	#  0x39 -> CONTROL
    u'\x9a'	#  0x3a -> CONTROL
    u'\x9b'	#  0x3b -> CONTROL
    u'\x14'	#  0x3c -> DEVICE CONTROL FOUR
    u'\x15'	#  0x3d -> NEGATIVE ACKNOWLEDGE
    u'\x9e'	#  0x3e -> CONTROL
    u'\x1a'	#  0x3f -> SUBSTITUTE
    u' '	#  0x40 -> SPACE
    u'\xa0'	#  0x41 -> NO-BREAK SPACE
    u'\xe2'	#  0x42 -> LATIN SMALL LETTER A WITH CIRCUMFLEX
    u'\xe4'	#  0x43 -> LATIN SMALL LETTER A WITH DIAERESIS
    u'\xe0'	#  0x44 -> LATIN SMALL LETTER A WITH GRAVE
    u'\xe1'	#  0x45 -> LATIN SMALL LETTER A WITH ACUTE
    u'\xe3'	#  0x46 -> LATIN SMALL LETTER A WITH TILDE
    u'\xe5'	#  0x47 -> LATIN SMALL LETTER A WITH RING ABOVE
    u'\xe7'	#  0x48 -> LATIN SMALL LETTER C WITH CEDILLA
    u'\xf1'	#  0x49 -> LATIN SMALL LETTER N WITH TILDE
    u'['	#  0x4a -> LEFT SQUARE BRACKET
    u'.'	#  0x4b -> FULL STOP
    u'<'	#  0x4c -> LESS-THAN SIGN
    u'('	#  0x4d -> LEFT PARENTHESIS
    u'+'	#  0x4e -> PLUS SIGN
    u'!'	#  0x4f -> EXCLAMATION MARK
    u'&'	#  0x50 -> AMPERSAND
    u'\xe9'	#  0x51 -> LATIN SMALL LETTER E WITH ACUTE
    u'\xea'	#  0x52 -> LATIN SMALL LETTER E WITH CIRCUMFLEX
    u'\xeb'	#  0x53 -> LATIN SMALL LETTER E WITH DIAERESIS
    u'\xe8'	#  0x54 -> LATIN SMALL LETTER E WITH GRAVE
    u'\xed'	#  0x55 -> LATIN SMALL LETTER I WITH ACUTE
    u'\xee'	#  0x56 -> LATIN SMALL LETTER I WITH CIRCUMFLEX
    u'\xef'	#  0x57 -> LATIN SMALL LETTER I WITH DIAERESIS
    u'\xec'	#  0x58 -> LATIN SMALL LETTER I WITH GRAVE
    u'\xdf'	#  0x59 -> LATIN SMALL LETTER SHARP S (GERMAN)
    u']'	#  0x5a -> RIGHT SQUARE BRACKET
    u'$'	#  0x5b -> DOLLAR SIGN
    u'*'	#  0x5c -> ASTERISK
    u')'	#  0x5d -> RIGHT PARENTHESIS
    u';'	#  0x5e -> SEMICOLON
    u'^'	#  0x5f -> CIRCUMFLEX ACCENT
    u'-'	#  0x60 -> HYPHEN-MINUS
    u'/'	#  0x61 -> SOLIDUS
    u'\xc2'	#  0x62 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    u'\xc4'	#  0x63 -> LATIN CAPITAL LETTER A WITH DIAERESIS
    u'\xc0'	#  0x64 -> LATIN CAPITAL LETTER A WITH GRAVE
    u'\xc1'	#  0x65 -> LATIN CAPITAL LETTER A WITH ACUTE
    u'\xc3'	#  0x66 -> LATIN CAPITAL LETTER A WITH TILDE
    u'\xc5'	#  0x67 -> LATIN CAPITAL LETTER A WITH RING ABOVE
    u'\xc7'	#  0x68 -> LATIN CAPITAL LETTER C WITH CEDILLA
    u'\xd1'	#  0x69 -> LATIN CAPITAL LETTER N WITH TILDE
    u'\xa6'	#  0x6a -> BROKEN BAR
    u','	#  0x6b -> COMMA
    u'%'	#  0x6c -> PERCENT SIGN
    u'_'	#  0x6d -> LOW LINE
    u'>'	#  0x6e -> GREATER-THAN SIGN
    u'?'	#  0x6f -> QUESTION MARK
    u'\xf8'	#  0x70 -> LATIN SMALL LETTER O WITH STROKE
    u'\xc9'	#  0x71 -> LATIN CAPITAL LETTER E WITH ACUTE
    u'\xca'	#  0x72 -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    u'\xcb'	#  0x73 -> LATIN CAPITAL LETTER E WITH DIAERESIS
    u'\xc8'	#  0x74 -> LATIN CAPITAL LETTER E WITH GRAVE
    u'\xcd'	#  0x75 -> LATIN CAPITAL LETTER I WITH ACUTE
    u'\xce'	#  0x76 -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    u'\xcf'	#  0x77 -> LATIN CAPITAL LETTER I WITH DIAERESIS
    u'\xcc'	#  0x78 -> LATIN CAPITAL LETTER I WITH GRAVE
    u'`'	#  0x79 -> GRAVE ACCENT
    u':'	#  0x7a -> COLON
    u'#'	#  0x7b -> NUMBER SIGN
    u'@'	#  0x7c -> COMMERCIAL AT
    u"'"	#  0x7d -> APOSTROPHE
    u'='	#  0x7e -> EQUALS SIGN
    u'"'	#  0x7f -> QUOTATION MARK
    u'\xd8'	#  0x80 -> LATIN CAPITAL LETTER O WITH STROKE
    u'a'	#  0x81 -> LATIN SMALL LETTER A
    u'b'	#  0x82 -> LATIN SMALL LETTER B
    u'c'	#  0x83 -> LATIN SMALL LETTER C
    u'd'	#  0x84 -> LATIN SMALL LETTER D
    u'e'	#  0x85 -> LATIN SMALL LETTER E
    u'f'	#  0x86 -> LATIN SMALL LETTER F
    u'g'	#  0x87 -> LATIN SMALL LETTER G
    u'h'	#  0x88 -> LATIN SMALL LETTER H
    u'i'	#  0x89 -> LATIN SMALL LETTER I
    u'\xab'	#  0x8a -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\xbb'	#  0x8b -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\xf0'	#  0x8c -> LATIN SMALL LETTER ETH (ICELANDIC)
    u'\xfd'	#  0x8d -> LATIN SMALL LETTER Y WITH ACUTE
    u'\xfe'	#  0x8e -> LATIN SMALL LETTER THORN (ICELANDIC)
    u'\xb1'	#  0x8f -> PLUS-MINUS SIGN
    u'\xb0'	#  0x90 -> DEGREE SIGN
    u'j'	#  0x91 -> LATIN SMALL LETTER J
    u'k'	#  0x92 -> LATIN SMALL LETTER K
    u'l'	#  0x93 -> LATIN SMALL LETTER L
    u'm'	#  0x94 -> LATIN SMALL LETTER M
    u'n'	#  0x95 -> LATIN SMALL LETTER N
    u'o'	#  0x96 -> LATIN SMALL LETTER O
    u'p'	#  0x97 -> LATIN SMALL LETTER P
    u'q'	#  0x98 -> LATIN SMALL LETTER Q
    u'r'	#  0x99 -> LATIN SMALL LETTER R
    u'\xaa'	#  0x9a -> FEMININE ORDINAL INDICATOR
    u'\xba'	#  0x9b -> MASCULINE ORDINAL INDICATOR
    u'\xe6'	#  0x9c -> LATIN SMALL LIGATURE AE
    u'\xb8'	#  0x9d -> CEDILLA
    u'\xc6'	#  0x9e -> LATIN CAPITAL LIGATURE AE
    u'\xa4'	#  0x9f -> CURRENCY SIGN
    u'\xb5'	#  0xa0 -> MICRO SIGN
    u'~'	#  0xa1 -> TILDE
    u's'	#  0xa2 -> LATIN SMALL LETTER S
    u't'	#  0xa3 -> LATIN SMALL LETTER T
    u'u'	#  0xa4 -> LATIN SMALL LETTER U
    u'v'	#  0xa5 -> LATIN SMALL LETTER V
    u'w'	#  0xa6 -> LATIN SMALL LETTER W
    u'x'	#  0xa7 -> LATIN SMALL LETTER X
    u'y'	#  0xa8 -> LATIN SMALL LETTER Y
    u'z'	#  0xa9 -> LATIN SMALL LETTER Z
    u'\xa1'	#  0xaa -> INVERTED EXCLAMATION MARK
    u'\xbf'	#  0xab -> INVERTED QUESTION MARK
    u'\xd0'	#  0xac -> LATIN CAPITAL LETTER ETH (ICELANDIC)
    u'\xdd'	#  0xad -> LATIN CAPITAL LETTER Y WITH ACUTE
    u'\xde'	#  0xae -> LATIN CAPITAL LETTER THORN (ICELANDIC)
    u'\xae'	#  0xaf -> REGISTERED SIGN
    u'\xa2'	#  0xb0 -> CENT SIGN
    u'\xa3'	#  0xb1 -> POUND SIGN
    u'\xa5'	#  0xb2 -> YEN SIGN
    u'\xb7'	#  0xb3 -> MIDDLE DOT
    u'\xa9'	#  0xb4 -> COPYRIGHT SIGN
    u'\xa7'	#  0xb5 -> SECTION SIGN
    u'\xb6'	#  0xb6 -> PILCROW SIGN
    u'\xbc'	#  0xb7 -> VULGAR FRACTION ONE QUARTER
    u'\xbd'	#  0xb8 -> VULGAR FRACTION ONE HALF
    u'\xbe'	#  0xb9 -> VULGAR FRACTION THREE QUARTERS
    u'\xac'	#  0xba -> NOT SIGN
    u'|'	#  0xbb -> VERTICAL LINE
    u'\xaf'	#  0xbc -> MACRON
    u'\xa8'	#  0xbd -> DIAERESIS
    u'\xb4'	#  0xbe -> ACUTE ACCENT
    u'\xd7'	#  0xbf -> MULTIPLICATION SIGN
    u'{'	#  0xc0 -> LEFT CURLY BRACKET
    u'A'	#  0xc1 -> LATIN CAPITAL LETTER A
    u'B'	#  0xc2 -> LATIN CAPITAL LETTER B
    u'C'	#  0xc3 -> LATIN CAPITAL LETTER C
    u'D'	#  0xc4 -> LATIN CAPITAL LETTER D
    u'E'	#  0xc5 -> LATIN CAPITAL LETTER E
    u'F'	#  0xc6 -> LATIN CAPITAL LETTER F
    u'G'	#  0xc7 -> LATIN CAPITAL LETTER G
    u'H'	#  0xc8 -> LATIN CAPITAL LETTER H
    u'I'	#  0xc9 -> LATIN CAPITAL LETTER I
    u'\xad'	#  0xca -> SOFT HYPHEN
    u'\xf4'	#  0xcb -> LATIN SMALL LETTER O WITH CIRCUMFLEX
    u'\xf6'	#  0xcc -> LATIN SMALL LETTER O WITH DIAERESIS
    u'\xf2'	#  0xcd -> LATIN SMALL LETTER O WITH GRAVE
    u'\xf3'	#  0xce -> LATIN SMALL LETTER O WITH ACUTE
    u'\xf5'	#  0xcf -> LATIN SMALL LETTER O WITH TILDE
    u'}'	#  0xd0 -> RIGHT CURLY BRACKET
    u'J'	#  0xd1 -> LATIN CAPITAL LETTER J
    u'K'	#  0xd2 -> LATIN CAPITAL LETTER K
    u'L'	#  0xd3 -> LATIN CAPITAL LETTER L
    u'M'	#  0xd4 -> LATIN CAPITAL LETTER M
    u'N'	#  0xd5 -> LATIN CAPITAL LETTER N
    u'O'	#  0xd6 -> LATIN CAPITAL LETTER O
    u'P'	#  0xd7 -> LATIN CAPITAL LETTER P
    u'Q'	#  0xd8 -> LATIN CAPITAL LETTER Q
    u'R'	#  0xd9 -> LATIN CAPITAL LETTER R
    u'\xb9'	#  0xda -> SUPERSCRIPT ONE
    u'\xfb'	#  0xdb -> LATIN SMALL LETTER U WITH CIRCUMFLEX
    u'\xfc'	#  0xdc -> LATIN SMALL LETTER U WITH DIAERESIS
    u'\xf9'	#  0xdd -> LATIN SMALL LETTER U WITH GRAVE
    u'\xfa'	#  0xde -> LATIN SMALL LETTER U WITH ACUTE
    u'\xff'	#  0xdf -> LATIN SMALL LETTER Y WITH DIAERESIS
    u'\\'	#  0xe0 -> REVERSE SOLIDUS
    u'\xf7'	#  0xe1 -> DIVISION SIGN
    u'S'	#  0xe2 -> LATIN CAPITAL LETTER S
    u'T'	#  0xe3 -> LATIN CAPITAL LETTER T
    u'U'	#  0xe4 -> LATIN CAPITAL LETTER U
    u'V'	#  0xe5 -> LATIN CAPITAL LETTER V
    u'W'	#  0xe6 -> LATIN CAPITAL LETTER W
    u'X'	#  0xe7 -> LATIN CAPITAL LETTER X
    u'Y'	#  0xe8 -> LATIN CAPITAL LETTER Y
    u'Z'	#  0xe9 -> LATIN CAPITAL LETTER Z
    u'\xb2'	#  0xea -> SUPERSCRIPT TWO
    u'\xd4'	#  0xeb -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    u'\xd6'	#  0xec -> LATIN CAPITAL LETTER O WITH DIAERESIS
    u'\xd2'	#  0xed -> LATIN CAPITAL LETTER O WITH GRAVE
    u'\xd3'	#  0xee -> LATIN CAPITAL LETTER O WITH ACUTE
    u'\xd5'	#  0xef -> LATIN CAPITAL LETTER O WITH TILDE
    u'0'	#  0xf0 -> DIGIT ZERO
    u'1'	#  0xf1 -> DIGIT ONE
    u'2'	#  0xf2 -> DIGIT TWO
    u'3'	#  0xf3 -> DIGIT THREE
    u'4'	#  0xf4 -> DIGIT FOUR
    u'5'	#  0xf5 -> DIGIT FIVE
    u'6'	#  0xf6 -> DIGIT SIX
    u'7'	#  0xf7 -> DIGIT SEVEN
    u'8'	#  0xf8 -> DIGIT EIGHT
    u'9'	#  0xf9 -> DIGIT NINE
    u'\xb3'	#  0xfa -> SUPERSCRIPT THREE
    u'\xdb'	#  0xfb -> LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    u'\xdc'	#  0xfc -> LATIN CAPITAL LETTER U WITH DIAERESIS
    u'\xd9'	#  0xfd -> LATIN CAPITAL LETTER U WITH GRAVE
    u'\xda'	#  0xfe -> LATIN CAPITAL LETTER U WITH ACUTE
    u'\x9f'	#  0xff -> CONTROL
)

### Encoding Map

encoding_map = {
    0x0000: 0x00,	#  NULL
    0x0001: 0x01,	#  START OF HEADING
    0x0002: 0x02,	#  START OF TEXT
    0x0003: 0x03,	#  END OF TEXT
    0x0004: 0x37,	#  END OF TRANSMISSION
    0x0005: 0x2d,	#  ENQUIRY
    0x0006: 0x2e,	#  ACKNOWLEDGE
    0x0007: 0x2f,	#  BELL
    0x0008: 0x16,	#  BACKSPACE
    0x0009: 0x05,	#  HORIZONTAL TABULATION
    0x000a: 0x25,	#  LINE FEED
    0x000b: 0x0b,	#  VERTICAL TABULATION
    0x000c: 0x0c,	#  FORM FEED
    0x000d: 0x0d,	#  CARRIAGE RETURN
    0x000e: 0x0e,	#  SHIFT OUT
    0x000f: 0x0f,	#  SHIFT IN
    0x0010: 0x10,	#  DATA LINK ESCAPE
    0x0011: 0x11,	#  DEVICE CONTROL ONE
    0x0012: 0x12,	#  DEVICE CONTROL TWO
    0x0013: 0x13,	#  DEVICE CONTROL THREE
    0x0014: 0x3c,	#  DEVICE CONTROL FOUR
    0x0015: 0x3d,	#  NEGATIVE ACKNOWLEDGE
    0x0016: 0x32,	#  SYNCHRONOUS IDLE
    0x0017: 0x26,	#  END OF TRANSMISSION BLOCK
    0x0018: 0x18,	#  CANCEL
    0x0019: 0x19,	#  END OF MEDIUM
    0x001a: 0x3f,	#  SUBSTITUTE
    0x001b: 0x27,	#  ESCAPE
    0x001c: 0x1c,	#  FILE SEPARATOR
    0x001d: 0x1d,	#  GROUP SEPARATOR
    0x001e: 0x1e,	#  RECORD SEPARATOR
    0x001f: 0x1f,	#  UNIT SEPARATOR
    0x0020: 0x40,	#  SPACE
    0x0021: 0x4f,	#  EXCLAMATION MARK
    0x0022: 0x7f,	#  QUOTATION MARK
    0x0023: 0x7b,	#  NUMBER SIGN
    0x0024: 0x5b,	#  DOLLAR SIGN
    0x0025: 0x6c,	#  PERCENT SIGN
    0x0026: 0x50,	#  AMPERSAND
    0x0027: 0x7d,	#  APOSTROPHE
    0x0028: 0x4d,	#  LEFT PARENTHESIS
    0x0029: 0x5d,	#  RIGHT PARENTHESIS
    0x002a: 0x5c,	#  ASTERISK
    0x002b: 0x4e,	#  PLUS SIGN
    0x002c: 0x6b,	#  COMMA
    0x002d: 0x60,	#  HYPHEN-MINUS
    0x002e: 0x4b,	#  FULL STOP
    0x002f: 0x61,	#  SOLIDUS
    0x0030: 0xf0,	#  DIGIT ZERO
    0x0031: 0xf1,	#  DIGIT ONE
    0x0032: 0xf2,	#  DIGIT TWO
    0x0033: 0xf3,	#  DIGIT THREE
    0x0034: 0xf4,	#  DIGIT FOUR
    0x0035: 0xf5,	#  DIGIT FIVE
    0x0036: 0xf6,	#  DIGIT SIX
    0x0037: 0xf7,	#  DIGIT SEVEN
    0x0038: 0xf8,	#  DIGIT EIGHT
    0x0039: 0xf9,	#  DIGIT NINE
    0x003a: 0x7a,	#  COLON
    0x003b: 0x5e,	#  SEMICOLON
    0x003c: 0x4c,	#  LESS-THAN SIGN
    0x003d: 0x7e,	#  EQUALS SIGN
    0x003e: 0x6e,	#  GREATER-THAN SIGN
    0x003f: 0x6f,	#  QUESTION MARK
    0x0040: 0x7c,	#  COMMERCIAL AT
    0x0041: 0xc1,	#  LATIN CAPITAL LETTER A
    0x0042: 0xc2,	#  LATIN CAPITAL LETTER B
    0x0043: 0xc3,	#  LATIN CAPITAL LETTER C
    0x0044: 0xc4,	#  LATIN CAPITAL LETTER D
    0x0045: 0xc5,	#  LATIN CAPITAL LETTER E
    0x0046: 0xc6,	#  LATIN CAPITAL LETTER F
    0x0047: 0xc7,	#  LATIN CAPITAL LETTER G
    0x0048: 0xc8,	#  LATIN CAPITAL LETTER H
    0x0049: 0xc9,	#  LATIN CAPITAL LETTER I
    0x004a: 0xd1,	#  LATIN CAPITAL LETTER J
    0x004b: 0xd2,	#  LATIN CAPITAL LETTER K
    0x004c: 0xd3,	#  LATIN CAPITAL LETTER L
    0x004d: 0xd4,	#  LATIN CAPITAL LETTER M
    0x004e: 0xd5,	#  LATIN CAPITAL LETTER N
    0x004f: 0xd6,	#  LATIN CAPITAL LETTER O
    0x0050: 0xd7,	#  LATIN CAPITAL LETTER P
    0x0051: 0xd8,	#  LATIN CAPITAL LETTER Q
    0x0052: 0xd9,	#  LATIN CAPITAL LETTER R
    0x0053: 0xe2,	#  LATIN CAPITAL LETTER S
    0x0054: 0xe3,	#  LATIN CAPITAL LETTER T
    0x0055: 0xe4,	#  LATIN CAPITAL LETTER U
    0x0056: 0xe5,	#  LATIN CAPITAL LETTER V
    0x0057: 0xe6,	#  LATIN CAPITAL LETTER W
    0x0058: 0xe7,	#  LATIN CAPITAL LETTER X
    0x0059: 0xe8,	#  LATIN CAPITAL LETTER Y
    0x005a: 0xe9,	#  LATIN CAPITAL LETTER Z
    0x005b: 0x4a,	#  LEFT SQUARE BRACKET
    0x005c: 0xe0,	#  REVERSE SOLIDUS
    0x005d: 0x5a,	#  RIGHT SQUARE BRACKET
    0x005e: 0x5f,	#  CIRCUMFLEX ACCENT
    0x005f: 0x6d,	#  LOW LINE
    0x0060: 0x79,	#  GRAVE ACCENT
    0x0061: 0x81,	#  LATIN SMALL LETTER A
    0x0062: 0x82,	#  LATIN SMALL LETTER B
    0x0063: 0x83,	#  LATIN SMALL LETTER C
    0x0064: 0x84,	#  LATIN SMALL LETTER D
    0x0065: 0x85,	#  LATIN SMALL LETTER E
    0x0066: 0x86,	#  LATIN SMALL LETTER F
    0x0067: 0x87,	#  LATIN SMALL LETTER G
    0x0068: 0x88,	#  LATIN SMALL LETTER H
    0x0069: 0x89,	#  LATIN SMALL LETTER I
    0x006a: 0x91,	#  LATIN SMALL LETTER J
    0x006b: 0x92,	#  LATIN SMALL LETTER K
    0x006c: 0x93,	#  LATIN SMALL LETTER L
    0x006d: 0x94,	#  LATIN SMALL LETTER M
    0x006e: 0x95,	#  LATIN SMALL LETTER N
    0x006f: 0x96,	#  LATIN SMALL LETTER O
    0x0070: 0x97,	#  LATIN SMALL LETTER P
    0x0071: 0x98,	#  LATIN SMALL LETTER Q
    0x0072: 0x99,	#  LATIN SMALL LETTER R
    0x0073: 0xa2,	#  LATIN SMALL LETTER S
    0x0074: 0xa3,	#  LATIN SMALL LETTER T
    0x0075: 0xa4,	#  LATIN SMALL LETTER U
    0x0076: 0xa5,	#  LATIN SMALL LETTER V
    0x0077: 0xa6,	#  LATIN SMALL LETTER W
    0x0078: 0xa7,	#  LATIN SMALL LETTER X
    0x0079: 0xa8,	#  LATIN SMALL LETTER Y
    0x007a: 0xa9,	#  LATIN SMALL LETTER Z
    0x007b: 0xc0,	#  LEFT CURLY BRACKET
    0x007c: 0xbb,	#  VERTICAL LINE
    0x007d: 0xd0,	#  RIGHT CURLY BRACKET
    0x007e: 0xa1,	#  TILDE
    0x007f: 0x07,	#  DELETE
    0x0080: 0x20,	#  CONTROL
    0x0081: 0x21,	#  CONTROL
    0x0082: 0x22,	#  CONTROL
    0x0083: 0x23,	#  CONTROL
    0x0084: 0x24,	#  CONTROL
    0x0085: 0x15,	#  CONTROL
    0x0086: 0x06,	#  CONTROL
    0x0087: 0x17,	#  CONTROL
    0x0088: 0x28,	#  CONTROL
    0x0089: 0x29,	#  CONTROL
    0x008a: 0x2a,	#  CONTROL
    0x008b: 0x2b,	#  CONTROL
    0x008c: 0x2c,	#  CONTROL
    0x008d: 0x09,	#  CONTROL
    0x008e: 0x0a,	#  CONTROL
    0x008f: 0x1b,	#  CONTROL
    0x0090: 0x30,	#  CONTROL
    0x0091: 0x31,	#  CONTROL
    0x0092: 0x1a,	#  CONTROL
    0x0093: 0x33,	#  CONTROL
    0x0094: 0x34,	#  CONTROL
    0x0095: 0x35,	#  CONTROL
    0x0096: 0x36,	#  CONTROL
    0x0097: 0x08,	#  CONTROL
    0x0098: 0x38,	#  CONTROL
    0x0099: 0x39,	#  CONTROL
    0x009a: 0x3a,	#  CONTROL
    0x009b: 0x3b,	#  CONTROL
    0x009c: 0x04,	#  CONTROL
    0x009d: 0x14,	#  CONTROL
    0x009e: 0x3e,	#  CONTROL
    0x009f: 0xff,	#  CONTROL
    0x00a0: 0x41,	#  NO-BREAK SPACE
    0x00a1: 0xaa,	#  INVERTED EXCLAMATION MARK
    0x00a2: 0xb0,	#  CENT SIGN
    0x00a3: 0xb1,	#  POUND SIGN
    0x00a4: 0x9f,	#  CURRENCY SIGN
    0x00a5: 0xb2,	#  YEN SIGN
    0x00a6: 0x6a,	#  BROKEN BAR
    0x00a7: 0xb5,	#  SECTION SIGN
    0x00a8: 0xbd,	#  DIAERESIS
    0x00a9: 0xb4,	#  COPYRIGHT SIGN
    0x00aa: 0x9a,	#  FEMININE ORDINAL INDICATOR
    0x00ab: 0x8a,	#  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00ac: 0xba,	#  NOT SIGN
    0x00ad: 0xca,	#  SOFT HYPHEN
    0x00ae: 0xaf,	#  REGISTERED SIGN
    0x00af: 0xbc,	#  MACRON
    0x00b0: 0x90,	#  DEGREE SIGN
    0x00b1: 0x8f,	#  PLUS-MINUS SIGN
    0x00b2: 0xea,	#  SUPERSCRIPT TWO
    0x00b3: 0xfa,	#  SUPERSCRIPT THREE
    0x00b4: 0xbe,	#  ACUTE ACCENT
    0x00b5: 0xa0,	#  MICRO SIGN
    0x00b6: 0xb6,	#  PILCROW SIGN
    0x00b7: 0xb3,	#  MIDDLE DOT
    0x00b8: 0x9d,	#  CEDILLA
    0x00b9: 0xda,	#  SUPERSCRIPT ONE
    0x00ba: 0x9b,	#  MASCULINE ORDINAL INDICATOR
    0x00bb: 0x8b,	#  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00bc: 0xb7,	#  VULGAR FRACTION ONE QUARTER
    0x00bd: 0xb8,	#  VULGAR FRACTION ONE HALF
    0x00be: 0xb9,	#  VULGAR FRACTION THREE QUARTERS
    0x00bf: 0xab,	#  INVERTED QUESTION MARK
    0x00c0: 0x64,	#  LATIN CAPITAL LETTER A WITH GRAVE
    0x00c1: 0x65,	#  LATIN CAPITAL LETTER A WITH ACUTE
    0x00c2: 0x62,	#  LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    0x00c3: 0x66,	#  LATIN CAPITAL LETTER A WITH TILDE
    0x00c4: 0x63,	#  LATIN CAPITAL LETTER A WITH DIAERESIS
    0x00c5: 0x67,	#  LATIN CAPITAL LETTER A WITH RING ABOVE
    0x00c6: 0x9e,	#  LATIN CAPITAL LIGATURE AE
    0x00c7: 0x68,	#  LATIN CAPITAL LETTER C WITH CEDILLA
    0x00c8: 0x74,	#  LATIN CAPITAL LETTER E WITH GRAVE
    0x00c9: 0x71,	#  LATIN CAPITAL LETTER E WITH ACUTE
    0x00ca: 0x72,	#  LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    0x00cb: 0x73,	#  LATIN CAPITAL LETTER E WITH DIAERESIS
    0x00cc: 0x78,	#  LATIN CAPITAL LETTER I WITH GRAVE
    0x00cd: 0x75,	#  LATIN CAPITAL LETTER I WITH ACUTE
    0x00ce: 0x76,	#  LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    0x00cf: 0x77,	#  LATIN CAPITAL LETTER I WITH DIAERESIS
    0x00d0: 0xac,	#  LATIN CAPITAL LETTER ETH (ICELANDIC)
    0x00d1: 0x69,	#  LATIN CAPITAL LETTER N WITH TILDE
    0x00d2: 0xed,	#  LATIN CAPITAL LETTER O WITH GRAVE
    0x00d3: 0xee,	#  LATIN CAPITAL LETTER O WITH ACUTE
    0x00d4: 0xeb,	#  LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    0x00d5: 0xef,	#  LATIN CAPITAL LETTER O WITH TILDE
    0x00d6: 0xec,	#  LATIN CAPITAL LETTER O WITH DIAERESIS
    0x00d7: 0xbf,	#  MULTIPLICATION SIGN
    0x00d8: 0x80,	#  LATIN CAPITAL LETTER O WITH STROKE
    0x00d9: 0xfd,	#  LATIN CAPITAL LETTER U WITH GRAVE
    0x00da: 0xfe,	#  LATIN CAPITAL LETTER U WITH ACUTE
    0x00db: 0xfb,	#  LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    0x00dc: 0xfc,	#  LATIN CAPITAL LETTER U WITH DIAERESIS
    0x00dd: 0xad,	#  LATIN CAPITAL LETTER Y WITH ACUTE
    0x00de: 0xae,	#  LATIN CAPITAL LETTER THORN (ICELANDIC)
    0x00df: 0x59,	#  LATIN SMALL LETTER SHARP S (GERMAN)
    0x00e0: 0x44,	#  LATIN SMALL LETTER A WITH GRAVE
    0x00e1: 0x45,	#  LATIN SMALL LETTER A WITH ACUTE
    0x00e2: 0x42,	#  LATIN SMALL LETTER A WITH CIRCUMFLEX
    0x00e3: 0x46,	#  LATIN SMALL LETTER A WITH TILDE
    0x00e4: 0x43,	#  LATIN SMALL LETTER A WITH DIAERESIS
    0x00e5: 0x47,	#  LATIN SMALL LETTER A WITH RING ABOVE
    0x00e6: 0x9c,	#  LATIN SMALL LIGATURE AE
    0x00e7: 0x48,	#  LATIN SMALL LETTER C WITH CEDILLA
    0x00e8: 0x54,	#  LATIN SMALL LETTER E WITH GRAVE
    0x00e9: 0x51,	#  LATIN SMALL LETTER E WITH ACUTE
    0x00ea: 0x52,	#  LATIN SMALL LETTER E WITH CIRCUMFLEX
    0x00eb: 0x53,	#  LATIN SMALL LETTER E WITH DIAERESIS
    0x00ec: 0x58,	#  LATIN SMALL LETTER I WITH GRAVE
    0x00ed: 0x55,	#  LATIN SMALL LETTER I WITH ACUTE
    0x00ee: 0x56,	#  LATIN SMALL LETTER I WITH CIRCUMFLEX
    0x00ef: 0x57,	#  LATIN SMALL LETTER I WITH DIAERESIS
    0x00f0: 0x8c,	#  LATIN SMALL LETTER ETH (ICELANDIC)
    0x00f1: 0x49,	#  LATIN SMALL LETTER N WITH TILDE
    0x00f2: 0xcd,	#  LATIN SMALL LETTER O WITH GRAVE
    0x00f3: 0xce,	#  LATIN SMALL LETTER O WITH ACUTE
    0x00f4: 0xcb,	#  LATIN SMALL LETTER O WITH CIRCUMFLEX
    0x00f5: 0xcf,	#  LATIN SMALL LETTER O WITH TILDE
    0x00f6: 0xcc,	#  LATIN SMALL LETTER O WITH DIAERESIS
    0x00f7: 0xe1,	#  DIVISION SIGN
    0x00f8: 0x70,	#  LATIN SMALL LETTER O WITH STROKE
    0x00f9: 0xdd,	#  LATIN SMALL LETTER U WITH GRAVE
    0x00fa: 0xde,	#  LATIN SMALL LETTER U WITH ACUTE
    0x00fb: 0xdb,	#  LATIN SMALL LETTER U WITH CIRCUMFLEX
    0x00fc: 0xdc,	#  LATIN SMALL LETTER U WITH DIAERESIS
    0x00fd: 0x8d,	#  LATIN SMALL LETTER Y WITH ACUTE
    0x00fe: 0x8e,	#  LATIN SMALL LETTER THORN (ICELANDIC)
    0x00ff: 0xdf,	#  LATIN SMALL LETTER Y WITH DIAERESIS
}