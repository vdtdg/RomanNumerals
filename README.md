# Roman Numeral Translator
From a TDD Kata => (https://codingdojo.org/kata/RomanNumerals/)[Instructions].

## Usage
From a python3 console.
```
>>> from RomanNumeralTranslator import RomanNumeralTranslator
```

### From Integer to Roman numerical 
```
>>> RomanNumeralTranslator.to_roman(3)
'III'
>>> RomanNumeralTranslator.to_roman(615)
'DCXV'
>>> RomanNumeralTranslator.to_roman(1492)
'MCDXCII'
```

### From Roman numerical to Integer 
```
>>> RomanNumeralTranslator.to_int('MCI')
1101
>>> RomanNumeralTranslator.to_int('XLII')
42
```