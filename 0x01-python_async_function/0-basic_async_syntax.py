#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10)-> float:
    """ a coroutine that takes an integer and waits for a random delay 
        between 0 and max_delay
    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        float: _description_
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
