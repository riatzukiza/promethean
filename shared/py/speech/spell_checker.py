"""Spell checker utilities."""

from transformers import T5ForConditionalGeneration, T5Tokenizer


# Load model and tokenizer once so that calls to ``correct`` are inexpensive.
model = T5ForConditionalGeneration.from_pretrained("Unbabel/gec-t5_small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")


def correct(sentence: str) -> str:
    """Return the grammar-corrected version of ``sentence``."""

    tokenized_sentence = tokenizer(
        "gec: " + sentence,
        max_length=128,
        truncation=True,
        padding="max_length",
        return_tensors="pt",
    )

    corrected_sentence = tokenizer.decode(
        model.generate(
            input_ids=tokenized_sentence.input_ids,
            attention_mask=tokenized_sentence.attention_mask,
            max_length=128,
            num_beams=5,
            early_stopping=True,
        )[0],
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True,
    )
    return corrected_sentence


def main() -> None:
    """Demonstrate the spell checker with a sample sentence."""

    sentence = "I can haz cheezburger"
    print(correct(sentence))  # -> I like swimming.


if __name__ == "__main__":
    main()
