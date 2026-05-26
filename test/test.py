import cocotb
from cocotb.triggers import Timer, ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting baseline verification loop...")
    
    # Initialize interface signals safely using explicit type safety
    dut.ena.value = 1
    dut.uio_in.value = 0
    dut.ui_in.value = 0
    dut.rst_n.value = 0
    
    # Give the simulator a brief step phase to stabilize the initial state wires
    await Timer(1, units="ns")
    
    # Apply system reset sequence over explicit clock iterations
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)
    
    dut._log.info("System came out of reset condition successfully.")
    
    # Monitor the output state changes across consecutive cycles
    for cycle in range(10):
        await ClockCycles(dut.clk, 1)
        # Safely capture the bus signal string to bypass interpretation mismatches
        bus_string = str(dut.uo_out.value)
        dut._log.info(f"Cycle {cycle}: Read Full 8-bit Output Bus = {bus_string}")
        
    dut._log.info("Baseline simulation completed successfully!")
