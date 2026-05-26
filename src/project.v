/*
 * Copyright (c) 2026 Satya Roop Bankuru
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    reg [7:0] shift_reg;
    wire feedback = shift_reg[7] ^ shift_reg[5] ^ shift_reg[4] ^ shift_reg[3];

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            shift_reg <= 8'h01; // Seed value
        end else begin
            shift_reg <= {shift_reg[6:0], feedback};
        end
    end

    // Direct assignment to the output bus
    assign uo_out = shift_reg;

    // Static tie-offs for bi-directional structures
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Unused input sinks to satisfy linters smoothly
    wire [7:0] dummy_wires = ui_in ^ uio_in;
    wire _unused = &{ena, dummy_wires, 1'b0};

endmodule
