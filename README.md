# 8-bit Pseudo-Random LFSR Generator (VLSI Training)

A Tiny Tapeout submission implementing an 8-bit Linear Feedback Shift Register (LFSR) pseudo-random number generator block.

## How it works
This design utilizes a maximal-period characteristic polynomial:
$$x^8 + x^6 + x^5 + x^4 + 1$$

On every rising edge of the system clock (`clk`), specific bit taps are XORed together to feed back into the shift register sequence, generating up to 255 unique state configurations before repeating.

## Pinout Map
* **Outputs (`uo_out[7:0]`)**: The active 8-bit pseudo-random byte.
* **Clock (`clk`)**: Advances the LFSR state.
* **Reset (`rst_n`)**: Active-low reset initializes the register to `0x01`.
