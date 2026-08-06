# EC Testability Interface Specification

This document defines the Embedded Controller (EC) testability interface for remote laptop testing.


The EC testability interface enables comprehensive remote testing of laptops by providing a simple console interface to control platform aspects like key presses, button presses, and power control.

## Interface Requirements

### Hardware Interface Options
- **SMBus Interface**: Primary communication channel for the testability interface
- **Parallel Interface**: Alternative communication channel for the testability interface

### BIOS Configuration

The interface requires a BIOS option to enable debugging features:

