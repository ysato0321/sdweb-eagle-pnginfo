from modules import prompt_parser, shared

class Parser:
    def prompt_to_tags(prompt):
        use_prompt_parser = shared.opts.use_prompt_parser_when_save_prompt_to_eagle_as_tags

        p = prompt
        if use_prompt_parser:
            parse_prompt_attention = getattr(prompt_parser, "parse_prompt_attention", None)
            if parse_prompt_attention is None:
                # Newer Neo versions moved attention parsing to the backend.
                from backend.text_processing.parsing import parse_prompt_attention

            p = ','.join(map(lambda x: x[0].strip(), parse_prompt_attention(p)))

        return [ x.strip() for x in p.split(",") if x.strip() != "" ]
