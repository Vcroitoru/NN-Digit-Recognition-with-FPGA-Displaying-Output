`timescale 1ns / 1ps

module display_controller_tb;

    // Testbench Signals
    reg clk;
    reg [3:0] gpio_digit;
    wire [6:0] seg;

    // Instantiate the display_controller module
    display_controller uut (
        .clk(clk),
        .gpio_digit(gpio_digit),
        .seg(seg)
    );

    // Clock generation (50MHz)
    initial begin
        clk = 0;
        forever #10 clk = ~clk;  // Toggle every 10ns
    end

    // Test sequence
    initial begin
        // Initialize
        gpio_digit = 4'b0000; // Start with digit '0'
        #100;                 // Wait 100ns for setup

        // Change the gpio_digit and check the seg output
        gpio_digit = 4'b0001; #20; // Test for digit '1'
        gpio_digit = 4'b0010; #20; // Test for digit '2'
        gpio_digit = 4'b0011; #20;
		  gpio_digit = 4'b0100; #20;
		  gpio_digit = 4'b0101; #20;
		  gpio_digit = 4'b0111; #20;
		  gpio_digit = 4'b1000; #20;
		  gpio_digit = 4'b1001; #20;
				 

        // Finish the test
        #100;
        $finish;
    end

endmodule
