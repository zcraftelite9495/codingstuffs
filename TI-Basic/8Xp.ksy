# The following KSY file shows the binary structure of 8XP files.
# These files are programs used on Texas TI-83 Plus and TI-84 Plus
# calculators.
meta:
  id: ti_8xp_file_format_template
  file-extension: 8XP File Format Template
  # Wherever two-byte integers are used, they are in LITTLE ENDIAN format
  # meaning that the least-significant byte comes first
  endian: le
  
# Here is the general structure of the file
# Each component is broken down further in the "types" section below.
seq:

  # Header is 55 bytes
  - id: header
    type: header
    size: 55
    doc: The header is always 55 bytes long
    
  # Meta data is 19 bytes
  - id: meta_data
    type: meta_data
    size: 19
    doc: The meta_data section is always 19 bytes long
    
  # Body is variable length (length is specified in the meta data above)
  - id: body
    type: program_body
    size: meta_data.body_length
    doc: |
      The length of the body is variable, and the number of
      bytes is specified inside meta_data.body_length
      
  # Checksum is always 2 bytes, at the very end of file
  - id: checksum
    type: u2 # Two-byte, unsigned integer
    doc: |
      All programs end with a 2 byte checksum.
      This is calculated by summing all the bytes in the meta_data and
      body sections (from byte 56 to the end, excluding checksum itself),
      and then taking the lower 16bits (2 bytes) of the answer, 
      in little endian form (which I think is the first two bytes of 
      the total).
      
types:

  # Here's a breakdown of what the 55 byte header contains:
  header:
    seq:
    
      - id: signature
        # contents: "**TI83F*"
        type: str
        size: 8
        # type: s8
        encoding: ASCII
        doc: Signature is usually these 8 chars: **TI83F*
        
      - id: signature_part_2
        contents: [0x1A, 0x0A] # two bytes, always with these values
        doc: The signature also generally includes these 2 bytes
        
      - id: mystery_byte
        type: u1 # single byte
        doc: |
          Either 0x00 or 0x0A? I've noticed that most TI-BASIC
          apps created with TI-Connect CE have this as 0x0A,
          while assembly apps compiled with Brass have it as
          0x00. Not sure if it makes any practical difference?
          To be confirmed.
          
      - id: comment
        size: 42
        type: str # string that is always 42 characters
        encoding: ASCII
        doc: |
          This can be anything, but is typically the version number of the
          app that compiled the 8XP file such as 
          "Created by TI Connect CE 5.6.3.2278"
          The remaining unused characters are filled with 0x00.
          
      - id: meta_and_body_length
        type: u2 # two bytes, unsigned integer, little endian
        doc: |
          Number of bytes from here on, excluding the checksum 
          (the final 2 bytes of file).
          This number should be 57 (39h) bytes less than the total file size.
  
  # Here's a breakdown of what the 19 byte meta data section contains:
  meta_data:
    seq:
    
      - id: flag
        type: u1 # single byte
        doc: |
          This appears to be some kind of flag/switch, where it's
          either 0x0B or 0x0D (0x0D on almost all apps I've inspected).
          Also 0x0D on groups.
          Not yet sure of the full meaning.
          
      - id: unknown
        type: u1 # single byte
        doc: |
          This appears to be 0x00 in most apps I've come across. 
          Unsure of purpose.
        
      - id: body_and_checksum_length
        type: u2 # two bytes, unsigned integer, little endian
        doc: Length of the body/code section and the 2 byte checksum, in bytes
        
      - id: file_type
        type: u1 # single byte
        enum: file_types # see file_types list at end of this spec
        doc: |
          05 for normal programs
          06 for edit-locked ones
          23 (0x17) for groups
          Almost all assembly programs have this as 06, presumably
          because you cannot easily edit these on a calculator.
          
      - id: program_name
        type: str # string that is always 8 characters
        size: 8
        encoding: ASCII
        doc: Maximum 8 chars. Unused characters are filled with 0x00.
        
      - id: version
        type: u1 # single byte
        doc: |
          Not sure what this actually does. 
          Appears to vary randomly across different apps, despite 
          them all being created with TI-Connect CE software. 
          I have seen:
            0x00
            0x04
            0x05
            0x06
            ...and 0x0B, however anything above 06 seems to cause an
            error in WabbitEmu emulator.
          Have seen it mentioned that it could be a version number,
          perhaps the version of TI-Basic or the version of the TI-OS
          needed to run the program (since some tokens/commands were
          introduced later).
          Apparently this field is present if the 
          "flag" (byte 55, 0x37) == $0D.
          
      - id: is_archived
        type: u1 # single byte
        enum: archived
        doc: 0x00 for normal apps, 0x80 for archived, apparently?
        
      - id: body_and_checksum_length_2
        type: u2 # two bytes, unsigned integer, little endian
        doc: |
          A redundant duplicate of the field above, containing the
          length of the body/code section and the 2 byte checksum, in bytes.
          Not sure why it is repeated again.
          
      - id: body_length
        type: u2 # two bytes, unsigned integer, little endian
        doc: |
          The length of the body *without* the checksum.
          It should be 2 bytes less than body_and_checksum_length.
          This is again a redundant measurement. Not sure
          which of the above is actually used on the calc.

  # The program body is a series of lines separated by the character
  # 0x3F.
  #
  # Note: if the first two bytes of the program body are 0xBB6D
  # then the program is an "assembly" program, not TI-BASIC
  # and it needs to be executed on the calc with Asm(prgmXXXX)
  #
  # I haven't implemented detection of individual tokens, as the list
  # is quite large. Lines are parsed, but not each token.
  program_body:
    seq:
      - id: lines
        type: str
        repeat: eos # continue reading line by line until we reach end of the program_body, based on its known length
        encoding: ASCII
        terminator: 0x3F # question mark character is used to end lines
        eos-error: false # the final line has no terminator, so we need to set this to false

# Here we store some of the magic flags as used above.
# Have not tested this template with all of the following types of files.
# Would be good to do that. ;-)
enums:
  file_types:
    0x05: program
    0x06: edit_locked_prgm
    0x17: group
    0x24: flash_application
  program_flag:
    0xBB6C: uncompiled_asm
    0xBB6D: compiled_asm
  archived:
    0x00: not_archived
    0x80: archived
