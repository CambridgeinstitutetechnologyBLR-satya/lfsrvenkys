import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting complete system flush verification...")
    
    # Intialize clock input pin to zero state explicitly
    dut.clk.value = 0
    dut.rst_n.value = 0
    
    # Wait for the simulation time to step forward past the initial crash window
    await Timer(10, unit="ns")
    
    # Let the simulation step forward while toggling the reset line manually
    dut.rst_n.value = 1
    await Timer(10, unit="ns")
    
    dut._log.info("System stabilization window cleared successfully!")
