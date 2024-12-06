"""
This module provides primitive operations to manage Python interpreters.
The 'interpreters' module provides a more convenient interface.
"""

from typing import Any, SupportsIndex

class QueueError(RuntimeError):
    """Indicates that a queue-related error happened."""
    ...
class QueueNotFoundError(QueueError): ...

def bind(qid: SupportsIndex) -> None:
    """
    bind(qid)

    Take a reference to the identified queue.
    The queue is not destroyed until there are no references left.
    """
    ...
def create(maxsize: SupportsIndex, fmt: SupportsIndex) -> int:
    """
    create(maxsize, fmt, unboundop) -> qid

    Create a new cross-interpreter queue and return its unique generated ID.
    It is a new reference as though bind() had been called on the queue.

    The caller is responsible for calling destroy() for the new queue
    before the runtime is finalized.
    """
    ...
def destroy(qid: SupportsIndex) -> None:
    """
    destroy(qid)

    Clear and destroy the queue.  Afterward attempts to use the queue
    will behave as though it never existed.
    """
    ...
def get(qid: SupportsIndex) -> tuple[Any, int]:
    """
    get(qid) -> (obj, fmt)

    Return a new object from the data at the front of the queue.
    The object's format is also returned.

    If there is nothing to receive then raise QueueEmpty.
    """
    ...
def get_count(qid: SupportsIndex) -> int:
    """
    get_count(qid)

    Return the number of items in the queue.
    """
    ...
def get_maxsize(qid: SupportsIndex) -> int:
    """
    get_maxsize(qid)

    Return the maximum number of items in the queue.
    """
    ...
def get_queue_defaults(qid: SupportsIndex) -> tuple[int]:
    """
    get_queue_defaults(qid)

    Return the queue's default values, set when it was created.
    """
    ...
def is_full(qid: SupportsIndex) -> bool:
    """
    is_full(qid)

    Return true if the queue has a maxsize and has reached it.
    """
    ...
def list_all() -> list[tuple[int, int]]:
    """
    list_all() -> [(qid, fmt)]

    Return the list of IDs for all queues.
    Each corresponding default format is also included.
    """
    ...
def put(qid: SupportsIndex, obj: Any, fmt: SupportsIndex) -> None:
    """
    put(qid, obj, fmt)

    Add the object's data to the queue.
    """
    ...
def release(qid: SupportsIndex) -> None:
    """
    release(qid)

    Release a reference to the queue.
    The queue is destroyed once there are no references left.
    """
    ...