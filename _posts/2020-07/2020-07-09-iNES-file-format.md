---
title: "iNES file format"
published: true
tags: Gaming
---

The iNES file format was originally defined by Marat Fayzullin for use in his
iNES emulator. The format has since been used by most emulators and is the most
common format for ROM images. INES format files should have the file extension
*.nes. The format provides a 16 byte header at the start of the file which
contains important information.

|Start Byte|Length (Bytes)|Contents|
|---|---|---|
|0|3|Should contain the string 'NES' to identify the file as an iNES file|
|3|1|Should contain the value $1A, also used to identify the file format|
|4|1|Number of 16 KB RPG-ROM banks. The RPG-ROM (Program ROM) is the area of ROM used to store the program code.|
|5|1|Number of 8 KB CHR-ROM / VROM banks. The names CHR-ROM (Character ROM) and VROM are used synonymously to refer to the area of ROM used to store graphics information, the pattern tables.|
|6|1|ROM Control Byte 1:<br> - Bit 0 - Indicates the type of mirroring use by the game where 0 indicate horizontal mirroring, 1 indicates vertical mirroring. <br> - Bit 1 - Indicates the presence of battery-backed RAM at memory locations $6000-$7FFF. <br> - Bit 2 - Indicates the presence of a 512-byte trainer at memory locations $7000-$71FF. <br> - Bit 3 - If this bit is set it overrides bit 0 to indicate four-screen mirroring should be used. <br> - Bit 4-7 - Four lower bits of the mapper number.|
|7|1|ROM Control Byte 2: <br> - Bit 0-3 - Reserved for future usage and should all be 0. <br> - Bit 4-7 - Four upper bits of the mapper number.|
|8|1|Number of 8 KB RAM banks. For compatibility with previous versions of the iNES format, assume 1 page of RAM when this is 0|
|9|7|Reserved for future usage and should all be 0.|


Following the header is the 512-byte trainer, if one is present, otherwise the
ROM banks begin here, starting with PRG-ROM then CHR-ROM. The format allows for
up to 256 different memory mappers. Each mapper is assigned a specific number
and the mapper number can be obtained by shifting bits 4-7 of control bytes 2 to
the left by 4 bits and then adding the bits 4-7 of control byte 1.