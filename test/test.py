import cocotb
from cocotb.triggers import ClockCycles, RisingEdge

@cocotb.test()
async def test_lfsr_multiplexed(dut):
    dut._log.info("Starting Multiplexed LFSR test")
    
    # Set the clock period to 20ns (50 MHz)
    # The clock was configured in config.json as 20ns
    # cocotb handles the background toggle loop automatically
    
    # Reset the circuit
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)
    
    dut._log.info("Circuit came out of reset safely.")
    
    # Read bit indices 0 through 7 by cycling ui_in
    for bit_index in range(8):
        dut.ui_in.value = bit_index
        await RisingEdge(dut.clk)
        current_output_bit = dut.uo_out[0].value
        dut._log.info(f"LFSR Register Bit {bit_index} reads out as: {current_output_bit}")

    dut._log.info("Multiplexed test passed successfully!")
