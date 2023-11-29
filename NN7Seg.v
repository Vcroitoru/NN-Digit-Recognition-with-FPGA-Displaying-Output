module arithmetic_led_display_controller(
    input clk,              // System clock
    input reset,            // Reset signal (active high)
    input [3:0] gpio_digit, // 4-bit input from GPIO pins
    input key3,             // Multiplication key
    input key2,             // Subtraction key
    input key1,             // Division key
    input key0,             // Addition key
    output reg [6:0] hex5,  // 7-segment display output for first digit
    output reg [6:0] hex3,  // 7-segment display output for second digit
    output reg [6:0] hex1,  // 7-segment display output for result (tens place)
    output reg [6:0] hex0,  // 7-segment display output for result (ones place)
    output [3:0] ledr       // LEDs for binary representation
);

reg [3:0] first_digit = 0;
reg [3:0] second_digit = 0;
reg [7:0] arithmetic_result = 0;
reg input_captured = 0;

// 7-segment encoding

wire [6:0] seven_seg_codes[9:0];
assign seven_seg_codes[0] = 7'b1000000; // '0'
assign seven_seg_codes[1] = 7'b1111001; // '1'
assign seven_seg_codes[2] = 7'b0100100; // '2'
assign seven_seg_codes[3] = 7'b0110000; // '3'
assign seven_seg_codes[4] = 7'b0011001; // '4'
assign seven_seg_codes[5] = 7'b0010010; // '5'
assign seven_seg_codes[6] = 7'b0000010; // '6'
assign seven_seg_codes[7] = 7'b1111000; // '7'
assign seven_seg_codes[8] = 7'b0000000; // '8'
assign seven_seg_codes[9] = 7'b0010000; // '9'


// State definitions
localparam WAIT = 2'b00, CAPTURE_FIRST = 2'b01, CAPTURE_SECOND = 2'b10;
reg [1:0] state = WAIT;

// Capture inputs and perform arithmetic operations
always @(posedge clk or posedge reset) begin
    if (reset) begin
        first_digit <= 0;
        second_digit <= 0;
        arithmetic_result <= 0;
        state <= WAIT;
    end else begin
        case (state)
            WAIT: begin
                state <= CAPTURE_FIRST;
            end
            CAPTURE_FIRST: begin
                first_digit <= gpio_digit;
                state <= CAPTURE_SECOND;
            end
            CAPTURE_SECOND: begin
                second_digit <= gpio_digit;
                if (!key3)  // Multiplication
                    arithmetic_result <= first_digit * second_digit;
                else if (!key2)  // Subtraction
                    arithmetic_result <= first_digit - second_digit;
                else if (!key1)  // Division (integer)
                    arithmetic_result <= (second_digit != 0) ? (first_digit / second_digit) : 0;
                else if (!key0)  // Addition
                    arithmetic_result <= first_digit + second_digit;
                else
                    arithmetic_result <= 0;  // Default case
            end
        endcase
    end
end

// Update the 7-segment displays
always @(*) begin
    hex5 <= seven_seg_codes[first_digit];
    hex1 <= seven_seg_codes[arithmetic_result / 10];  // Tens place
    hex3 <= seven_seg_codes[second_digit];
    hex0 <= seven_seg_codes[arithmetic_result % 10];  // Ones place
end

// Update the LEDs with the binary value from gpio_digit
assign ledr = gpio_digit;

endmodule

