#include <stdint.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <stdio.h>

#define GPIO_BASE 0x0300B000
#define PAGE_SIZE 0x1000  // 4KB

// Bank offsets for H618
uint32_t bankOffsets(char bank) {
    switch(bank) {
        case 'C': return 0x48;   // 2*0x24
        case 'H': return 0x108;  // 7*0x24
        case 'I': return 0x120;  // 8*0x24
        default: return 0;
    }
}

// CFG register for pin
uint32_t getCfgAddress(char bank, int pin) {
    uint32_t base = GPIO_BASE;
    uint32_t bankOffset = bankOffsets(bank);
    int regIndex = pin / 8;           // CFG0..CFG3
    return base + bankOffset + regIndex * 4;
}

int getShift(int pin) {
    return (pin % 8) * 4;
}

// Simple WriteReg function
void WriteReg(uint32_t physAddr, uint32_t value) {
    int fd = open("/dev/mem", O_RDWR | O_SYNC);
    if(fd < 0) { perror("open"); return; }

    void* map = mmap(nullptr, PAGE_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, physAddr & ~0xFFF);
    if(map == MAP_FAILED) { perror("mmap"); close(fd); return; }

    volatile uint32_t* reg = (uint32_t*)((char*)map + (physAddr & 0xFFF));
    *reg = value;

    munmap(map, PAGE_SIZE);
    close(fd);
}

// Set pin as output
void pinModeOutput(char bank, int pin) {
    uint32_t cfgAddr = getCfgAddress(bank, pin);
    int shift = getShift(pin);

    // read current register
    int fd = open("/dev/mem", O_RDWR | O_SYNC);
    if(fd < 0) { perror("open"); return; }

    void* map = mmap(nullptr, PAGE_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, cfgAddr & ~0xFFF);
    if(map == MAP_FAILED) { perror("mmap"); close(fd); return; }

    volatile uint32_t* reg = (uint32_t*)((char*)map + (cfgAddr & 0xFFF));

    // clear old 4 bits, set output
    *reg &= ~(0xF << shift);
    *reg |= (1 << shift);

    munmap(map, PAGE_SIZE);
    close(fd);
}

// Write HIGH/LOW to pin
void digitalWrite(char bank, int pin, int state) {
    uint32_t datAddr = GPIO_BASE + bankOffsets(bank) + 0x10;  // DAT register offset
    if(state)
        WriteReg(datAddr, 1 << pin);    // HIGH
    else
        WriteReg(datAddr, 0 << pin);    // LOW
}

// Example usage
//*int main() {
    char bank = 'I';
    int pin = 4;

    pinModeOutput(bank, pin);   // PI4 output
    while(1<10){
        digitalWrite(bank, pin, 1); // PI4 HIGH
        usleep(1);
        digitalWrite(bank, pin, 0); // PI4 LOW
        usleep(750);
    }
    return 0;
}*//
