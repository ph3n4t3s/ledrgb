/**
 * Version analogique
 * 
 * Varie de 0 à 1023
 */
/**
 * Version analogique
 * 
 * Varie de 0 à 1023
 * 
 * A REMPLACER dans le bloc au démarrage
 */
/**
 * La led est connectée à 3 broches (ports)
 * 
 * - P0 : La couleur rouge
 * 
 * - P1 : La couleur verte
 * 
 * - P2 : La couleur bleue
 */
pins.digitalWritePin(DigitalPin.P0, 0)
pins.digitalWritePin(DigitalPin.P1, 0)
pins.digitalWritePin(DigitalPin.P2, 0)
/**
 * Version numérique
 * 
 * Varie entre 0 à 1
 */
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P2, 0)
})
