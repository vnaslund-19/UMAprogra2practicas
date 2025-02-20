#!/usr/bin/env python3
#-----------------------------------------------------------------------
#Author: Vicente Benjumea
#Creation time: 2023/08/28 11:28:08
#Modification time: 2024/07/22 15:31:30
#-----------------------------------------------------------------------
__author__ = "Vicente Benjumea"
__version__ = "2024.07.22.15.31.30"
#-----------------------------------------------------------------------
"""Módulo de operaciones de soporte para unittesting.

- ChkNames = typing.NamedTuple("ChkNames", (("falta", list[str]), ("extra", list[str])))

- chkObjVarNames(obj, ref_names, *, rem_prefix) -> ChkNames:
    Compara los nombres de atributos del objeto con los nombres de ref_names,
    y devuelve los nombres que faltan y los nombres extras. Elimina de
    los nombres extras aquellos que comienzan por los prefijos especificados
    en rem_prefix.

- chkObjFunNames(obj, ref_names, *, rem_prefix) -> ChkNames:
    Compara los nombres de metodos del objeto con los nombres de ref_names,
    y devuelve los nombres que faltan y los nombres extras. Elimina de
    los nombres extras aquellos que comienzan por los prefijos especificados
    en rem_prefix.

- chkFunParNames(function, ref_names, *, rem_prefix) -> ChkNames:
    Compara los nombres de parametros de la funcion con los nombres de ref_names,
    y devuelve los nombres que faltan y los nombres extras. Elimina de
    los nombres extras aquellos que comienzan por los prefijos especificados
    en rem_prefix.

- chkattrprfx(obj: object, prefix: (str|typing.Iterable[str]), number: int) -> bool:
    Comprueba la cantidad de atributos, y el prefijo del nombre de
    los atributos.

- normdata(data: typing.Any, *,
           nrmitm: Optional[dict[type,typing.Callable[[typing.Any], typing.Any]]] = None) -> list:
    devuelve los datos normalizados. Es de utilidad para comparar
    estructuras de datos con los valores esperados.

- flattendata(data: typing.Any, *,
                level: int = -1) -> list[tuple]:
    devuelve una lista aplanada de tuplas con los elementos de
    data. Es de utilidad para comparar estructuras de datos con los
    valores esperados. En caso de set y dict, las tuplas de la lista
    seran ordenadas. level==0 no se aplana. level negativo, aplana
    todos los niveles. level positivo aplana ese numero de niveles.

- str2normsp(string: str, *,
             sp: typing.Optional[str] = None,
             nl: typing.Optional[str] = None,
             stripmode: str = "rstrip") -> str:
    Devuelve el string con espacios normalizados.
    Cada línea rstrip espacios según arg STRIPMODE.
    Reemplaza espacios por arg SP.
    Reemplaza saltos de linea por arg NL.

- str2ascii(string: str) -> str:
    devuelve el string normalizado ascii

- str2tk(string: str, *,
         lower: bool = None,           # convert strings to lower-case
         cnvt_ascii: bool = None,      # convert strings to ascii
         rem_nalnum: bool = None,      # remove all not alpha&numbers tokens
         rem_nnum: bool = None,        # remove all not number tokens
         rem_in: str = None,           # remove tokens in rem_in
         rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers
         rem_nin: str = None,          # remove tokens not in rem_nin
         sort_all: bool = None,        # sort all tokens
         sort_begin: str = None,       # sorted region beginning token
         sort_end: str = None) -> str: # sorted region ending token
    devuelve el string normalizado tokens

- str2tkref(string: str, reference: str, *,
            lower: bool = None,           # convert strings to lower-case
            cnvt_ascii: bool = None,      # convert strings to ascii
            rem_nalnum: bool = None,      # remove all not alpha&numbers tokens
            rem_nnum: bool = None,        # remove all not number tokens
            rem_in: str = None,           # remove tokens in rem_in
            rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers (si existe, añade str2tk(reference))
            rem_nin: str = None,          # remove tokens not in rem_nin (si existe, añade str2tk(reference))
            sort_all: bool = None,        # sort all tokens
            sort_begin: str = None,       # sorted region beginning token
            sort_end: str = None) -> tuple[str,str]: # sorted region ending token
    devuelve el string y reference normalizado tokens

- str2tkalnum(string: str, *,
              lower: bool = None,           # convert strings to lower-case
              rem_in: str = None,           # remove tokens in rem_in
              rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers
              rem_nin: str = None,          # remove tokens not in rem_nin
              sort_all: bool = None,        # sort all tokens
              sort_begin: str = None,       # sorted region beginning token
              sort_end: str = None) -> str: # sorted region ending token
    devuelve el string normalizado tokens alpha-ascii&numbers

- str2tkalnumref(string: str, reference: str, *,
                 lower: bool = None,           # convert strings to lower-case
                 rem_in: str = None,           # remove tokens in rem_in
                 rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers (si existe, añade str2tk(reference))
                 rem_nin: str = None,          # remove tokens not in rem_nin (si existe, añade str2tk(reference))
                 sort_all: bool = None,        # sort all tokens
                 sort_begin: str = None,       # sorted region beginning token
                 sort_end: str = None) -> tuple[str,str]: # sorted region ending token
    devuelve el string y reference normalizado tokens alpha-ascii&numbers

- str2tkascii(string: str, *,
              lower: bool = None,           # convert strings to lower-case
              rem_nalnum: bool = None,      # remove all not alpha&numbers tokens
              rem_in: str = None,           # remove tokens in rem_in
              rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers
              rem_nin: str = None,          # remove tokens not in rem_nin
              sort_all: bool = None,        # sort all tokens
              sort_begin: str = None,       # sorted region beginning token
              sort_end: str = None) -> str: # sorted region ending token
    devuelve el string normalizado tokens ascii

- str2tkasciiref(string: str, reference: str, *,
                 lower: bool = None,           # convert strings to lower-case
                 rem_nalnum: bool = None,      # remove all not alpha&numbers tokens
                 rem_in: str = None,           # remove tokens in rem_in
                 rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers (si existe, añade str2tk(reference))
                 rem_nin: str = None,          # remove tokens not in rem_nin (si existe, añade str2tk(reference))
                 sort_all: bool = None,        # sort all tokens
                 sort_begin: str = None,       # sorted region beginning token
                 sort_end: str = None) -> tuple[str,str]: # sorted region ending token
    devuelve el string y reference normalizado tokens ascii

- str2tknumber(string: str, *,
               rem_in: str = None,           # remove tokens in rem_in
               rem_nin: str = None,          # remove tokens not in rem_nin
               sort_all: bool = None,        # sort all tokens
               sort_begin: str = None,       # sorted region beginning token
               sort_end: str = None) -> str: # sorted region ending token
    devuelve el string normalizado tokens de números

- str2tknumberref(string: str, reference: str, *,
                  rem_in: str = None,           # remove tokens in rem_in
                  rem_nin: str = None,          # remove tokens not in rem_nin (si existe, añade str2tk(reference))
                  sort_all: bool = None,        # sort all tokens
                  sort_begin: str = None,       # sorted region beginning token
                  sort_end: str = None) -> tuple[str,str]: # sorted region ending token
    devuelve el string y reference normalizado tokens de números

- file2str(filename: str) -> str:
    devuelve el string con el contenido del fichero (o str(exc))

- str2file(filename: str, contenido: str) -> bool:
    escribe el contenido en el fichero especificado

- remove_file(filename: str) -> bool:
    elimina el fichero especificado

- with IOCapture("1\n2\n3\n4\n") as io_capture:
        print("Introduce valores")
        v1 = int(input("Valor 1"))
        print("Resultado:", v1)
    print(io_capture.get_stdout_value())
    print(io_capture.get_stderr_value())

"""
#-----------------------------------------------------------------------
import io
import sys
import re
import typing
import types
#import typing_extensions
import inspect
import unittest
#import unittest.util
import logging
import traceback
import signal
import threading
import functools
import os
import os.path
import unicodedata
#-----------------------------------------------------------------------
#-- WatchDogTimer ------------------------------------------------------
#-----------------------------------------------------------------------
DEF_TEST_TIMEOUT = 15 # segundos
#-----------------------------------------------------------------------
# Timeout Error
#-----------------------------------
class TimeoutError(BaseException):
    """Timeout error."""
    pass
#-----------------------------------------------------------------------
# En Python, el manejador de señal solo se puede establecer desde la
# "hebra principal", y cuando se recibe una señal, solo la maneja la
# "hebra principal", por lo que este metodo no es adecuado para
# interrumpir programas con multuiples hebras, o multiples procesos.
#-----------------------------------------------------------------------
# POSIX: SIGABRT, SIGINT, SIGQUIT, SIGTERM, SIGUSR1,  SIGUSR2
# WIndows: SIGABRT, SIGINT, SIGTERM, SIGBREAK
#-----------------------------------
# Timeout Context Manager
#-----------------------------------
class TimeoutCtx:
    """Timeout context manager. When time expires, the execution of
    context statements is aborted by raising the Timeout Error
    exception."""
    def __init__(self, seconds: int, *args, **kwargs) -> None:
        self.__seconds = seconds
        self.__timer = None
        self.__old_sighandler = None
        super().__init__(*args, **kwargs)

    def __raise_exception(self, *args, **kwargs) -> None:
        #print(f"DBG TimeoutCtx __raise_exception thread: {threading.get_ident()}")
        raise TimeoutError("Timeout")

    def __timer_callback(self, *args, **kwargs) -> None:
        #print(f"DBG TimeoutCtx __timer_callback thread: {threading.get_ident()}")
        signal.raise_signal(signal.SIGABRT)

    def __enter__(self) -> 'TimeoutCtx':
        #print(f"DBG TimeoutCtx enter thread: {threading.get_ident()}")
        self.__old_sighandler = signal.signal(signal.SIGABRT, self.__raise_exception)
        self.__timer = threading.Timer(self.__seconds, self.__timer_callback)
        self.__timer.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        #print(f"DBG TimeoutCtx exit  thread: {threading.get_ident()}")
        self.__timer.cancel()
        signal.signal(signal.SIGABRT, self.__old_sighandler)
        self.__timer.join()
        self.__timer = None
        self.__old_sighandler = None
        return None
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Timeout function decorator
#-----------------------------------
def Timeout(seconds: int):
    """Function decorator. The decorated function will raise a Timeout
    exception if its execution time exceeds the specified timeout."""
    def wrapper(func):
        @functools.wraps(func)
        def func_timeout_wrapper(*args, **kwargs):
            with TimeoutCtx(seconds):
                return func(*args, **kwargs)
        return func_timeout_wrapper
    return wrapper
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
# https://docs.python.org/es/3/library/stdtypes.html#special-attributes
# https://docs.python.org/3/reference/datamodel.html#user-defined-functions
# https://docs.python.org/3/library/inspect.html
#-----------------------------------------------------------------------
#-- UnitTestError ------------------------------------------------------
#-----------------------------------------------------------------------
class UnitTestError(RuntimeError):
    """AssertionError shows errors in tested code.
    UnitTestError shows errors in testing code."""
    pass
#-----------------------------------------------------------------------
#-- Introspection ------------------------------------------------------
#-----------------------------------------------------------------------
def chkattrprfx(obj: object, prefix: (str|typing.Iterable[str]), number: int) -> bool:
    """Comprueba la cantidad de atributos, y el prefijo del nombre de
    los atributos."""
    if hasattr(obj, "__dict__"):
        curr_names = tuple(vars(obj).keys())
    elif hasattr(obj, "_fields"):
        curr_names = tuple(obj._fields)
    else:
        curr_names = tuple()
    attrnnmbr = len(curr_names)
    if isinstance(prefix, str):
        prefix = [prefix]
    return ((attrnnmbr == number)
            and all(any(nm.startswith(pfx) for pfx in prefix) for nm in curr_names))
#-----------------------------------------------------------------------
ChkNames = typing.NamedTuple("ChkNames", (("falta", list[str]), ("extra", list[str])))
#-----------------------------------------------------------------------
def _chkNameSeqs(curr_names: typing.Sequence[str],
                 ref_names: typing.Sequence[str], *,
                 rem_prefix: typing.Optional[str|typing.Sequence[str]] = None) -> ChkNames:
    """Compara las secuencias de nombres curr_names con ref_names,
    y devuelve los nombres que faltan y los nombres extras en/de
    curr_names. Elimina de los nombres extras aquellos que comienzan
    por los prefijos especificados en rem_prefix"""
    if not isinstance(ref_names, (tuple,list,set)):
        raise UnitTestError("ref-names-arg is not a sequence")
    if not isinstance(curr_names, (tuple,list,set)):
        raise UnitTestError("curr-names-arg is not a sequence")
    names_falta = list()
    names_extra = list()
    for nm in ref_names:
        if nm not in curr_names:
            names_falta.append(nm)
    for nm in curr_names:
        if nm not in ref_names:
            names_extra.append(nm)
    if isinstance(rem_prefix, (str)):
        rem_prefix = [rem_prefix]
    if isinstance(rem_prefix, (tuple,list,set)):
        #names_extra = [nm for nm in names_extra if not any(nm.startswith(pfx) for pfx in rem_prefix)]
        for nmprfx in rem_prefix:
            names_extra = [nm for nm in names_extra if not nm.startswith(nmprfx)]
    return ChkNames(falta=names_falta, extra=names_extra)
#-----------------------------------------------------------------------
def chkObjVarNames(obj, ref_names: typing.Sequence[str], *,
                   rem_prefix: typing.Optional[str|typing.Sequence[str]] = None) -> ChkNames:
    """Compara los nombres de atributos del objeto con los nombres de ref_names,
    y devuelve los nombres que faltan y los nombres extras. Elimina de
    los nombres extras aquellos que comienzan por los prefijos especificados
    en rem_prefix"""
    try:
        # curr_names = tuple(name for (name, value) in inspect.getmembers(obj))
        if hasattr(obj, "__dict__"):
            curr_names = tuple(vars(obj).keys())
        elif hasattr(obj, "_fields"):
            curr_names = obj._fields
        else:
            curr_names = tuple()
    except (ValueError, TypeError, AttributeError):
        curr_names = tuple()
    return _chkNameSeqs(curr_names=curr_names, ref_names=ref_names, rem_prefix=rem_prefix)
#-----------------------------------------------------------------------
def chkObjFunNames(obj, ref_names: typing.Sequence[str], *,
                   rem_prefix: typing.Optional[str|typing.Sequence[str]] = None) -> ChkNames:
    """Compara los nombres de metodos del objeto con los nombres de ref_names,
    y devuelve los nombres que faltan y los nombres extras. Elimina de
    los nombres extras aquellos que comienzan por los prefijos especificados
    en rem_prefix"""
    curr_names = tuple(name for (name, value) in inspect.getmembers(obj, inspect.ismethod))
    return _chkNameSeqs(curr_names=curr_names, ref_names=ref_names, rem_prefix=rem_prefix)
#-----------------------------------------------------------------------
def chkFunParNames(function, ref_names: typing.Sequence[str], *,
                   rem_prefix: typing.Optional[str|typing.Sequence[str]] = None) -> ChkNames:
    """Compara los nombres de parametros de la funcion con los nombres de ref_names,
    y devuelve los nombres que faltan y los nombres extras. Elimina de
    los nombres extras aquellos que comienzan por los prefijos especificados
    en rem_prefix"""
    curr_names = None
    if inspect.isfunction(function) or inspect.ismethod(function):
        argspec = inspect.getfullargspec(function)
        curr_names = list()
        if isinstance(argspec.args, list):
            curr_names.extend(argspec.args)
        if isinstance(argspec.varargs, str):
            curr_names.append(argspec.varargs)
        if isinstance(argspec.varkw, str):
            curr_names.append(argspec.varkw)
        if isinstance(argspec.kwonlyargs, list):
            curr_names.extend(argspec.kwonlyargs)
    if curr_names is None:
        raise UnitTestError("function-arg is not a function/method")
    return _chkNameSeqs(curr_names=curr_names, ref_names=ref_names, rem_prefix=rem_prefix)
#-----------------------------------------------------------------------
#-- Normalizar Data. ---------------------------------------------------
#-----------------------------------------------------------------------
def _sort_items(iterable: typing.Iterable) -> typing.Iterable:
    try:
        elementos: typing.Iterable = sorted(iterable)
    except TypeError:
        elementos = iterable
    return elementos
#-----------------------------------------------------------------------
def _normitem(item: typing.Any,
              prfxtp: bool,
              nrmitm: dict[type,typing.Callable[[typing.Any], typing.Any]],
              stackobjs: set[typing.Any]) -> typing.Any:
    """devuelve el item normalizado"""
    if item is None:
        nuevo_item = item
    elif type(item) in nrmitm:
        nitm = nrmitm.get(type(item))
        if nitm is None:
            nuevo_item = item
        else:
            try:
                nuevo_item = nitm(item)
            except Exception as exc:
                #nuevo_item = item
                nuevo_item = f"Error: [{exc!r}]"
    elif isinstance(item, (bool, int, float, complex, str)):
        nuevo_item = item
    elif id(item) in stackobjs:
        # es un objeto recursivo, que se referencia a si mismo
        # se reemplaza por un valor fijo para evitar ciclos infinitos
        # también se podria reemplazar por un codigo hash
        nuevo_item = "objeto#$@recursivo"
    else:
        stackobjs.add(id(item))
        if isinstance(item, tuple):
            nuevo_item = tuple(_normitem(it, prfxtp, nrmitm, stackobjs) for it in item)
        elif isinstance(item, list):
            nuevo_item = list(_normitem(it, prfxtp, nrmitm, stackobjs) for it in item)
        elif isinstance(item, set):
            nuevo_item = list(_sort_items(_normitem(it, prfxtp, nrmitm, stackobjs) for it in item))
            if prfxtp:
                nuevo_item = (type(item).__name__, nuevo_item)
        elif isinstance(item, dict):
            nuevo_item = list(_sort_items(_normitem(it, prfxtp, nrmitm, stackobjs) for it in item.items()))
            if prfxtp:
                nuevo_item = (type(item).__name__, nuevo_item)
        elif hasattr(item, "__dict__"):
            nuevo_item = tuple(_normitem(v, prfxtp, nrmitm, stackobjs) for (k,v) in sorted(vars(item).items()))
            if prfxtp:
                nuevo_item = (type(item).__name__, nuevo_item)
        else:
            nuevo_item = item
        stackobjs.discard(id(item))
    return nuevo_item    
#-----------------------------------
def normdata(data: typing.Any, *,
             prfxtp: bool = True,
             nrmitm: typing.Optional[dict[type,typing.Callable[[typing.Any], typing.Any]]] = None) -> list:
    """devuelve los datos normalizados. Es de utilidad para comparar
    estructuras de datos con los valores esperados."""
    if nrmitm is None:
        nrmitm = dict()
    if not isinstance(nrmitm, dict):
        raise ValueError(f"normdata.nrmitm not a dict [{type(nrmitm).__name__}]")
    stackobjs: set[typing.Any] = set()
    return _normitem(data, prfxtp, nrmitm, stackobjs)
#-----------------------------------------------------------------------
#-- Aplanar Data. Generar Lista de Tuplas ---------------------------
#-----------------------------------------------------------------------
def flattendata(data: typing.Any, *,
                level: int = -1) -> list:
    """devuelve una lista aplanada con los elementos de data. Es de
    utilidad para comparar estructuras de datos con los valores
    esperados. En caso de set y dict, los elementos seran
    ordenados. level==0 no se aplana. level negativo, aplana todos los
    niveles. level positivo aplana ese numero de niveles."""
    if isinstance(data, (tuple, list)):
        lista = list()
        for item in data:
            if (level != 0) and isinstance(item, (tuple, list, set, dict)):
                lista.extend(flattendata(item, level=level-1))
            else:
                lista.append(item)
    elif isinstance(data, set):
        lista = list()
        for item in _sort_items(data):
            if (level != 0) and isinstance(item, (tuple, list, set, dict)):
                lista.extend(flattendata(item, level=level-1))
            else:
                lista.append(item)
    elif isinstance(data, dict):
        lista = list()
        for (key, value) in _sort_items(data.items()):
            if (level != 0):
                lista.extend(flattendata(key, level=level-1))
                lista.extend(flattendata(value, level=level-1))
                #it0 = flattendata(key, level=level-1)
                #it1 = flattendata(value, level=level-1)
                #lista.append((*it0, *it1))
            else:
                lista.append( (key, value) )
    else:
        lista = [ data ]
    return lista
#-----------------------------------------------------------------------
#-- String transformation ----------------------------------------------
#-----------------------------------------------------------------------
_CHARMAP = {
    #----
    "\n": " ",      # newline
    "\r": " ",      # return
    "\t": " ",      # tabulator
    "\f": " ",      # form-feed
    "\u20AC": "$",  #  €
    "\u03BC": "@",  #  µ
    #----
    "\u00A0": " ",  #  space
    "\u00A1": "!",  #  ¡
    "\u00A2": "$",  #  ¢
    "\u00A3": "$",  #  £
    "\u00A4": "#",  #  ¤
    "\u00A5": "$",  #  ¥
    "\u00A6": "|",  #  ¦
    "\u00A7": "$",  #  §
    "\u00A8": '"',  #  ¨
    "\u00A9": "@",  #  ©
    "\u00AA": "@",  #  ª
    "\u00AB": "<",  #  «
    "\u00AC": "~",  #  ¬
    "\u00AD": "-",  #  ­
    "\u00AE": "@",  #  ®
    "\u00AF": "-",  #  ¯
    #----
    "\u00B0": "@",  #  °
    "\u00B1": "#",  #  ±
    "\u00B2": "#",  #  ²
    "\u00B3": "#",  #  ³
    "\u00B4": "'",  #  ´
    "\u00B5": "@",  #  µ
    "\u00B6": "$",  #  ¶
    "\u00B7": ".",  #  ·
    "\u00B8": ",",  #  ¸
    "\u00B9": "#",  #  ¹
    "\u00BA": "@",  #  º
    "\u00BB": ">",  #  »
    "\u00BC": "#",  #  ¼
    "\u00BD": "#",  #  ½
    "\u00BE": "#",  #  ¾
    "\u00BF": "?",  #  ¿ 
    #----
    "\u00C0": "A",  #  À
    "\u00C1": "A",  #  Á
    "\u00C2": "A",  #  Â
    "\u00C3": "A",  #  Ã
    "\u00C4": "A",  #  Ä
    "\u00C5": "A",  #  Å
    "\u00C6": "A",  #  Æ
    "\u00C7": "C",  #  Ç
    "\u00C8": "E",  #  È
    "\u00C9": "E",  #  É
    "\u00CA": "E",  #  Ê
    "\u00CB": "E",  #  Ë
    "\u00CC": "I",  #  Ì
    "\u00CD": "I",  #  Í
    "\u00CE": "I",  #  Î
    "\u00CF": "I",  #  Ï
    #----
    "\u00D0": "D",  #  Ð
    "\u00D1": "N",  #  Ñ
    "\u00D2": "O",  #  Ò
    "\u00D3": "O",  #  Ó
    "\u00D4": "O",  #  Ô
    "\u00D5": "O",  #  Õ
    "\u00D6": "O",  #  Ö
    "\u00D7": "*",  #  ×
    "\u00D8": "#",  #  Ø
    "\u00D9": "U",  #  Ù
    "\u00DA": "U",  #  Ú
    "\u00DB": "U",  #  Û
    "\u00DC": "U",  #  Ü
    "\u00DD": "Y",  #  Ý
    "\u00DE": "Z",  #  Þ
    "\u00DF": "S",  #  ß
    #----
    "\u00E0": "a",  #  à
    "\u00E1": "a",  #  á
    "\u00E2": "a",  #  â
    "\u00E3": "a",  #  ã
    "\u00E4": "a",  #  ä
    "\u00E5": "a",  #  å
    "\u00E6": "a",  #  æ
    "\u00E7": "c",  #  ç
    "\u00E8": "e",  #  è
    "\u00E9": "e",  #  é
    "\u00EA": "e",  #  ê
    "\u00EB": "e",  #  ë
    "\u00EC": "i",  #  ì
    "\u00ED": "i",  #  í
    "\u00EE": "i",  #  î
    "\u00EF": "i",  #  ï
    #----
    "\u00F0": "d",  #  ð
    "\u00F1": "n",  #  ñ
    "\u00F2": "o",  #  ò
    "\u00F3": "o",  #  ó
    "\u00F4": "o",  #  ô
    "\u00F5": "o",  #  õ
    "\u00F6": "o",  #  ö
    "\u00F7": "/",  #  ÷
    "\u00F8": "#",  #  ø
    "\u00F9": "u",  #  ù
    "\u00FA": "u",  #  ú
    "\u00FB": "u",  #  û
    "\u00FC": "u",  #  ü
    "\u00FD": "y",  #  ý
    "\u00FE": "z",  #  þ
    "\u00FF": "y",  #  ÿ
}
#-----------------------------------------------------------------------
def strstrip(linea: str, stripmode: str) -> str:
    match stripmode:
        case "rstrip":
            resultado = linea.rstrip()
        case "lstrip":
            resultado = linea.lstrip()
        case "strip":
            resultado = linea.strip()
        case _:
            resultado = linea
    return resultado
#-----------------------------------------------------------------------
def str2normsp(string: str, *,
               sp: typing.Optional[str] = None,
               nl: typing.Optional[str] = None,
               stripmode: str = "rstrip") -> str:
    """Devuelve el string con espacios normalizados.
    Cada línea rstrip espacios según arg STRIPMODE.
    Reemplaza espacios por arg SP.
    Reemplaza saltos de linea por arg NL."""
    if isinstance(nl, str):
        nlsymbol = nl
    else:
        nlsymbol = "\n"
    if isinstance(sp, str):
        spsymbol = sp
    else:
        spsymbol = " "
    return nlsymbol.join([strstrip(linea, stripmode).replace(" ", spsymbol) for linea in string.splitlines()]) + nlsymbol
#-----------------------------------------------------------------------
def str2ascii(string: str) -> str:
    """convierte un string a caracteres ascii"""
    res = string
    if isinstance(string, str):
        string = unicodedata.normalize("NFKC", string)
        with io.StringIO() as strmanip:
            for ch in string:
                ch2 = _CHARMAP.get(ch, ch)
                if ((ord(ch2) < ord(" ")) or (ord(ch2) > ord("~"))):
                    if (ord(ch2) in {768, 769, 770, 771, 772, 776, 778, 807}):
                        ch2 = ""
                    else:
                        ch2 = " "
                strmanip.write(ch2)
            res = strmanip.getvalue()
    return res
#-----------------------------------------------------------------------
def str2lower(string: str) -> str:
    """convierte un string a lower-case"""
    res = string
    if isinstance(string, str):
        res = string.lower()
    return res
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
# https://docs.python.org/3/library/re.html#writing-a-tokenizer
def _tokenize_string(string):
    token_specification = [
        ( "TOKEN_NEWLINE", r'\n' ),
        ( "TOKEN_SKIP", r'[ \t]+' ),
        ( "TOKEN_LETTER", r'[A-Za-zÁÉÍÓÚÜÑÇáéíóúüñç]+' ),
        ( "TOKEN_NUMBER", r'([-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)' ),
        ( "TOKEN_OTHER", r'.'),            # Any other character
    ]
    #tok_regex = '|'.join(f"(?P<{pair[0]}>{pair[1]})" for pair in token_specification)
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    #scan_regex = re.compile(tok_regex, flags=re.MULTILINE)
    scan_regex = re.compile(tok_regex, flags=0)
    for mo in scan_regex.finditer(string):
        kind = mo.lastgroup
        value = mo.group()
        if ((kind != 'TOKEN_NEWLINE') and (kind != "TOKEN_SKIP")):
            if kind == "TOKEN_NUMBER":
                if (('e' in value)or('E' in value)):
                    #value = str(round(float(value), 7)) # formato punto fijo
                    value = f"{float(value):.6e}"
                elif ('.' in value):
                    #value = str(round(float(value), 7)) # formato punto fijo
                    value = f"{float(value):.6f}"
            yield value
    return
#-----------------------------------------------------------------------
def _buscar_sublista(lista: list[int], sublista: list[int], inicio: int = 0) -> int:
    len_sublista = len(sublista)
    if (0 < len_sublista <= len(lista)-inicio):
        if len_sublista == 1:
            idx = lista.index(sublista[0], inicio)
        else:
            idx = inicio-1
            encontrado = False
            while not encontrado:
                idx = lista.index(sublista[0], idx+1)
                encontrado = (sublista == lista[idx:idx+len_sublista])
    else:
        raise ValueError("sublist is not in list")
    return idx
#-----------------------------------------------------------------------
# def _sort_regions(tkstr, sort_begin: str, sort_end: str) -> list[str]:
#     sort_begin = next(_tokenize_string(sort_begin)) # el primer token
#     sort_end = next(_tokenize_string(sort_end))     # el primer token
#     #-------------------------------
#     lista_tkstr = list(tkstr)
#     try:
#         idx1 = lista_tkstr.index(sort_begin)
#         idx2 = lista_tkstr.index(sort_end, idx1+1)
#         while ((idx1 >= 0) and (idx2 >= 0)):
#             lista_tkstr[idx1+1:idx2] = sorted(lista_tkstr[idx1+1:idx2])
#             idx1 = lista_tkstr.index(sort_begin, idx2+1)
#             idx2 = lista_tkstr.index(sort_end, idx1+1)
#     except ValueError as exc:
#         pass # idx1 o idx2 no encontrado, terminar procesamiento
#     return lista_tkstr
#-----------------------------------
# def _sort_regions(tkstr, sort_begin: str, sort_end: str) -> list[str]:
#     sort_begin = next(_tokenize_string(sort_begin)) # el primer token
#     sort_end = next(_tokenize_string(sort_end))     # el primer token
#     #-------------------------------
#     lista_tkstr = list(tkstr)
#     try:
#         idx2 = -1
#         while True:
#             idx1 = lista_tkstr.index(sort_begin, idx2+1)
#             idx2 = lista_tkstr.index(sort_end, idx1+1)
#             lista_tkstr[idx1+1:idx2] = sorted(lista_tkstr[idx1+1:idx2])
#     except ValueError as exc:
#         pass # idx1 o idx2 no encontrado, terminar procesamiento
#     return lista_tkstr
#-----------------------------------
def _sort_regions(tkstr, sort_begin: str, sort_end: str) -> list[str]:
    sort_begin = list(_tokenize_string(sort_begin))
    sort_end = list(_tokenize_string(sort_end))
    lista_tkstr = list(tkstr)
    len_sort_begin = len(sort_begin)
    len_sort_end = len(sort_end)
    try:
        idx2 = -len_sort_end
        while True:
            idx1 = _buscar_sublista(lista_tkstr, sort_begin, idx2+len_sort_end)
            idx2 = _buscar_sublista(lista_tkstr, sort_end, idx1+len_sort_begin)
            lista_tkstr[idx1+len_sort_begin:idx2] = sorted(lista_tkstr[idx1+len_sort_begin:idx2])
    except ValueError as exc:
        pass # idx1 o idx2 no encontrado, terminar procesamiento
    return lista_tkstr
#-----------------------------------------------------------------------
# def str2tk(string: str) -> str:
#     """convierte un string a tokens (normaliza separadores)"""
#     res = string
#     if isinstance(string, str):
#         res = " ".join(_tokenize_string(string))
#     return res
#-----------------------------------------------------------------------
def _isnumber(string: str) -> bool:
    return ((len(string) > 0)
            and((string[0].isdecimal())
                or (string[0] == '-' and (len(string) > 1) and string[1].isdecimal())))
#-----------------------------------------------------------------------
def _isalphanumber(string: str) -> bool:
    return ((len(string) > 0)
            and((string[0].isalnum())
                or (string[0] == '-' and (len(string) > 1) and string[1].isdecimal())))
#-----------------------------------------------------------------------
def str2tk(string: str, *,
           lower: bool = None,           # convert strings to lower-case
           cnvt_ascii: bool = None,      # convert strings to ascii
           rem_nalnum: bool = None,      # remove all not alpha&numbers tokens
           rem_nnum: bool = None,        # remove all not number tokens
           rem_in: str = None,           # remove tokens in rem_in
           rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers
           rem_nin: str = None,          # remove tokens not in rem_nin
           sort_all: bool = None,        # sort all tokens
           sort_begin: str = None,       # sorted region beginning token
           sort_end: str = None) -> str: # sorted region ending token
    """convierte un string a tokens (normaliza separadores).
    - lower: si True entonces convierte string a lower-case.
    - cnvt_ascii: si True entonces convierte string a ascii.
    - rem_nalnum: keep alpha&numbers, remove others
    - rem_nnum: si True entonces elimina los no-números.
    - rem_in: elimina los tokens en rem_in.
    - rem_ninkn: elimina tokens no-en rem_ninkn, pero mantiene los numeros
    - rem_nin: elimina tokens no-en rem_nin
    - sort_all: sort all tokens
    - sort_begin: sorted region beginning token
    - sort_end: sorted region ending token
      token regions among sort_begin and sort_end will be sorted. This
      is useful when comparing sets
      region sorting is carried-out before any token removal
    """
    res = string
    if isinstance(string, str):
        #---------------------------
        if cnvt_ascii is True:
            string = str2ascii(string)
            rem_in = str2ascii(rem_in)
            rem_ninkn = str2ascii(rem_ninkn)
            rem_nin = str2ascii(rem_nin)
            sort_begin = str2ascii(sort_begin)
            sort_end = str2ascii(sort_end)
        #---------------------------
        if lower is True:
            string = str2lower(string)
            rem_in = str2lower(rem_in)
            rem_ninkn = str2lower(rem_ninkn)
            rem_nin = str2lower(rem_nin)
            sort_begin = str2lower(sort_begin)
            sort_end = str2lower(sort_end)
        #---------------------------
        tkstr = _tokenize_string(string)
        #---------------------------
        if sort_all:
            tkstr = sorted(tkstr)
        elif ((sort_begin is not None) and (sort_end is not None)):
            tkstr = _sort_regions(tkstr, sort_begin, sort_end)
        #---------------------------
        if rem_nnum is True:
            tkstr = (tk for tk in tkstr if _isnumber(tk))
        elif rem_nalnum is True:
            tkstr = (tk for tk in tkstr if _isalphanumber(tk))
        #---------------------------
        if (isinstance(rem_in, str) and (len(rem_in) > 0)):
            tkremin = set(_tokenize_string(rem_in))
            if (len(tkremin) > 0):
                tkstr = (tk for tk in tkstr if tk not in tkremin)
        if (isinstance(rem_ninkn, str) and (len(rem_ninkn) > 0)):
            tkkpin = set(_tokenize_string(rem_ninkn))
            if (len(tkkpin) > 0):
                tkstr = (tk for tk in tkstr if ((_isnumber(tk))or(tk in tkkpin)))
        if (isinstance(rem_nin, str) and (len(rem_nin) > 0)):
            tkkpin = set(_tokenize_string(rem_nin))
            if (len(tkkpin) > 0):
                tkstr = (tk for tk in tkstr if (tk in tkkpin))
        res = " ".join(tkstr)
    return res
#-----------------------------------------------------------------------
def str2tkref(string: str, reference: str, *,
              lower: bool = None,           # convert strings to lower-case
              cnvt_ascii: bool = None,      # convert strings to ascii
              rem_nalnum: bool = None,      # remove all not alpha&numbers tokens
              rem_nnum: bool = None,        # remove all not number tokens
              rem_in: str = None,           # remove tokens in rem_in
              rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers (si existe, añade str2tk(reference))
              rem_nin: str = None,          # remove tokens not in rem_nin (si existe, añade str2tk(reference))
              sort_all: bool = None,        # sort all tokens
              sort_begin: str = None,       # sorted region beginning token
              sort_end: str = None) -> tuple[str,str]: # sorted region ending token
    """convierte un string y reference a tokens (normaliza separadores).
    - lower: si True entonces convierte string a lower-case.
    - cnvt_ascii: si True entonces convierte string a ascii.
    - rem_nalnum: keep alpha&numbers, remove others
    - rem_nnum: si True entonces elimina los no-números.
    - rem_in: elimina los tokens en rem_in.
    - rem_ninkn: elimina tokens no-en rem_ninkn, pero mantiene los numeros (si existe, añade str2tk(reference))
    - rem_nin: elimina tokens no-en rem_nin (si existe, añade str2tk(reference))
    - sort_all: sort all tokens
    - sort_begin: sorted region beginning token
    - sort_end: sorted region ending token
      token regions among sort_begin and sort_end will be sorted. This
      is useful when comparing sets
      region sorting is carried-out before any token removal
    """
    if (isinstance(rem_ninkn, str)):
        rem_ninkn += " " + reference
    if (isinstance(rem_nin, str)):
        rem_nin += " " + reference
    new_ref = str2tk(reference,
                     lower=lower,
                     cnvt_ascii=cnvt_ascii,
                     rem_nalnum=rem_nalnum,
                     rem_nnum=rem_nnum,
                     rem_in=rem_in,
                     rem_ninkn=rem_ninkn,
                     rem_nin=rem_nin,
                     sort_all=sort_all,
                     sort_begin=sort_begin,
                     sort_end=sort_end)
    new_str = str2tk(string,
                     lower=lower,
                     cnvt_ascii=cnvt_ascii,
                     rem_nalnum=rem_nalnum,
                     rem_nnum=rem_nnum,
                     rem_in=rem_in,
                     rem_ninkn=rem_ninkn,
                     rem_nin=rem_nin,
                     sort_all=sort_all,
                     sort_begin=sort_begin,
                     sort_end=sort_end)
    return (new_str, new_ref)
#-----------------------------------------------------------------------
def str2tknumber(string: str, *,
                 rem_in: str = None,           # remove tokens in rem_in
                 rem_nin: str = None,          # remove tokens not in rem_nin
                 sort_all: bool = None,        # sort all tokens
                 sort_begin: str = None,       # sorted region beginning token
                 sort_end: str = None) -> str: # sorted region ending token
    """convierte un string a tokens de números (normaliza
    separadores). Elimina token in rem_in. Elimina token not in
    rem_nin"""
    return str2tk(string,
                  rem_nnum=True,
                  rem_in=rem_in,
                  rem_nin=rem_nin,
                  sort_all=sort_all,
                  sort_begin=sort_begin,
                  sort_end=sort_end)
#-----------------------------------------------------------------------
def str2tknumberref(string: str, reference: str, *,
                    rem_in: str = None,           # remove tokens in rem_in
                    rem_nin: str = None,          # remove tokens not in rem_nin (si existe, añade str2tk(reference))
                    sort_all: bool = None,        # sort all tokens
                    sort_begin: str = None,       # sorted region beginning token
                    sort_end: str = None) -> tuple[str,str]: # sorted region ending token
    """convierte un string y referencia a tokens de números (normaliza
    separadores). Elimina token in rem_in. Elimina token not in
    rem_nin"""
    return str2tkref(string, reference,
                     rem_nnum=True,
                     rem_in=rem_in,
                     rem_nin=rem_nin,
                     sort_all=sort_all,
                     sort_begin=sort_begin,
                     sort_end=sort_end)
#-----------------------------------------------------------------------
def str2tkascii(string: str, *,
                lower: bool = None,           # convert strings to lower-case
                rem_nalnum: bool = None,      # remove all not alpha&numbers tokens
                rem_in: str = None,           # remove tokens in rem_in
                rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers
                rem_nin: str = None,          # remove tokens not in rem_nin
                sort_all: bool = None,        # sort all tokens
                sort_begin: str = None,       # sorted region beginning token
                sort_end: str = None) -> str: # sorted region ending token
    """convierte un string a tokens ascii (normaliza
    separadores). Elimina token in rem_in. Elimina token not in
    rem_ninkn (mantiene numeros). Elimina token not in rem_nin"""
    return str2tk(string,
                  lower=lower,
                  cnvt_ascii=True,
                  rem_nalnum=rem_nalnum,
                  rem_in=rem_in,
                  rem_ninkn=rem_ninkn,
                  rem_nin=rem_nin,
                  sort_all=sort_all,
                  sort_begin=sort_begin,
                  sort_end=sort_end)
#-----------------------------------------------------------------------
def str2tkasciiref(string: str, reference: str, *,
                   lower: bool = None,           # convert strings to lower-case
                   rem_nalnum: bool = None,      # remove all not alpha&numbers tokens
                   rem_in: str = None,           # remove tokens in rem_in
                   rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers (si existe, añade str2tk(reference))
                   rem_nin: str = None,          # remove tokens not in rem_nin (si existe, añade str2tk(reference))
                   sort_all: bool = None,        # sort all tokens
                   sort_begin: str = None,       # sorted region beginning token
                   sort_end: str = None) -> tuple[str,str]: # sorted region ending token
    """convierte un string y referencia a tokens ascii (normaliza
    separadores). Elimina token in rem_in. Elimina token not in
    rem_ninkn (mantiene numeros). Elimina token not in rem_nin"""
    return str2tkref(string, reference,
                     lower=lower,
                     cnvt_ascii=True,
                     rem_nalnum=rem_nalnum,
                     rem_in=rem_in,
                     rem_ninkn=rem_ninkn,
                     rem_nin=rem_nin,
                     sort_all=sort_all,
                     sort_begin=sort_begin,
                     sort_end=sort_end)
#-----------------------------------------------------------------------
def str2tkalnum(string: str, *,
                lower: bool = None,           # convert strings to lower-case
                rem_in: str = None,           # remove tokens in rem_in
                rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers
                rem_nin: str = None,          # remove tokens not in rem_nin
                sort_all: bool = None,        # sort all tokens
                sort_begin: str = None,       # sorted region beginning token
                sort_end: str = None) -> str: # sorted region ending token
    """convierte un string a tokens alpha-ascii&numbers (normaliza
    separadores). Elimina token in rem_in. Elimina token not in
    rem_ninkn (mantiene numeros). Elimina token not in rem_nin"""
    return str2tk(string,
                  lower=lower,
                  cnvt_ascii=True,
                  rem_nalnum=True,
                  rem_in=rem_in,
                  rem_ninkn=rem_ninkn,
                  rem_nin=rem_nin,
                  sort_all=sort_all,
                  sort_begin=sort_begin,
                  sort_end=sort_end)
#-----------------------------------------------------------------------
def str2tkalnumref(string: str, reference: str, *,
                   lower: bool = None,           # convert strings to lower-case
                   rem_in: str = None,           # remove tokens in rem_in
                   rem_ninkn: str = None,        # remove tokens not in rem_ninkn, but keep numbers (si existe, añade str2tk(reference))
                   rem_nin: str = None,          # remove tokens not in rem_nin (si existe, añade str2tk(reference))
                   sort_all: bool = None,        # sort all tokens
                   sort_begin: str = None,       # sorted region beginning token
                   sort_end: str = None) -> tuple[str,str]: # sorted region ending token
    """convierte un string y referencia a tokens alpha-ascii&numbers (normaliza
    separadores). Elimina token in rem_in. Elimina token not in
    rem_ninkn (mantiene numeros). Elimina token not in rem_nin"""
    return str2tkref(string, reference,
                     lower=lower,
                     cnvt_ascii=True,
                     rem_nalnum=True,
                     rem_in=rem_in,
                     rem_ninkn=rem_ninkn,
                     rem_nin=rem_nin,
                     sort_all=sort_all,
                     sort_begin=sort_begin,
                     sort_end=sort_end)
#-----------------------------------------------------------------------
#-- Operaciones con ficheros -------------------------------------------
#-----------------------------------------------------------------------
def file2str(filename: str) -> str:
    try:
        with open(os.path.normpath(filename), "r", encoding="utf-8") as file:
            res = file.read()
    except (ValueError, OSError) as exc:
        res = repr(exc)
    return res
#-----------------------------------
def str2file(filename: str, contenido: str) -> bool:
    try:
        res = False
        with open(os.path.normpath(filename), "w", encoding="utf-8") as file:
            file.write(contenido)
            if ((len(contenido) > 0) and (contenido[-1] != "\n")):
                file.write("\n")
        res = True
    except (ValueError, OSError) as exc:
        res = False
    return res
#-----------------------------------
def remove_file(filename: str) -> bool:
    try:
        res = False
        os.remove(filename)
    except (ValueError, OSError) as exc:
        res = False
    else:
        res = True
    return res
#-----------------------------------------------------------------------
#-- Class IOCapture ContextManager -------------------------------------
#-----------------------------------------------------------------------
class IOCapture:
    """Captura sys.stdout, sys.stderr y sys.stdin"""
    def __init__(self, invalue: typing.Optional[str] = None, *args, **kwargs) -> None:
        """recibe el valor inicial para sys.stdin"""
        self.__invalue = invalue
        if not isinstance(self.__invalue, str):
            self.__invalue = ""
        if not self.__invalue.endswith('\n'):
            self.__invalue += '\n'
        self.__stdin_org = sys.stdin
        self.__stdout_org = sys.stdout
        self.__stderr_org = sys.stderr
        self.__stdin: typing.Optional[io.StringIO] = None
        self.__stdout: typing.Optional[io.StringIO] = None
        self.__stderr: typing.Optional[io.StringIO] = None
        self.__stdout_value: typing.Optional[str] = None
        self.__stderr_value: typing.Optional[str] = None
        super().__init__(*args, **kwargs)
    
    def __enter__(self) -> 'IOCapture':
        self.__stdout_value = None
        self.__stderr_value = None
        self.__stdin = io.StringIO(self.__invalue)
        self.__stdout = io.StringIO()
        self.__stderr = io.StringIO()
        
        sys.stdin = self.__stdin
        sys.stdout = self.__stdout
        sys.stderr = self.__stderr
        
        return self

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        sys.stdin = self.__stdin_org
        sys.stdout = self.__stdout_org
        sys.stderr = self.__stderr_org

        self.__stdout_value = self.__stdout.getvalue()
        self.__stderr_value = self.__stderr.getvalue()

        self.__stdin.close()
        self.__stdout.close()
        self.__stderr.close()
        
        del self.__stdin    # release memory
        del self.__stdout   # release memory
        del self.__stderr   # release memory

        return None

    def get_stdout_value(self) -> typing.Optional[str]:
        """devuelve el string capturado de sys.stdout"""
        return self.__stdout_value
    
    def get_stderr_value(self) -> typing.Optional[str]:
        """devuelve el string capturado de sys.stderr"""
        return self.__stderr_value
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
