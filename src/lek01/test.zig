// TODO: uzraksti testu, lai parbaudītu cik ātri strādā zig ar lieliem csv
// Basic usage

const zcsv = @import("zcsv");
const std = @import("std");

// ...

// Get an allocator
var gpa = std.heap.GeneralPurposeAllocator(.{}){};
defer _ = gpa.deinit();
const allocator = gpa.allocator();

// Get a reader
const stdin = std.io.getStdIn().reader();

// Make a parse
// If we want to copy headers, simply change map_sk to map_ck
// We need a try since we will try to parse the headers immediately, which may fail
var parser = try zcsv.allocs.map.init(allocator, stdin, .{});
// Note: map parsers must be deinitialized!
// They are the only parsers (currently) which need to be deinitialized
defer parser.deinit();

// We're building a list of user structs
var res = std.ArrayList(User).init(alloc);
errdefer res.deinit();

// Iterate over rows
const fieldToInt = zcsv.decode.fieldToInt;
while (parser.next) |row| {
    defer row.deinit();

    // Validate we have our columns
    const id = row.data().get("userid") orelse return error.MissingUserId;
    const name = row.data().get("name") orelse return error.MissingName;
    const age = row.data().get("age") orelse return error.MissingAge;

    // Validate and parse our user
    try res.append(User{
        .id = fieldToInt(i64, id, 10) catch {
            return error.InvalidUserId;
        } orelse return error.MissingUserId,
        .name = try name.clone(allocator),
        .age = fieldToInt(u16, age, 10) catch return error.InvalidAge,
    });
}