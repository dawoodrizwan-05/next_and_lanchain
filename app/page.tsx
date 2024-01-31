'use client';
 // Add the 'use client' pragma at the beginning of the file

import React, { useState } from 'react';

const page = () => {
  const [messages, setMessages] = useState<string[]>([]); // Explicitly specify the type as string[]
  const [inputValue, setInputValue] = useState('');

  const handleSend = () => {
    if (inputValue.trim() !== '') {
      setMessages((prevMessages) => [...prevMessages, inputValue]);
      setInputValue('');
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };
  const handleClearChat = () => {
    setMessages([]);
  };
  return (
    <div className="flex h-screen antialiased text-gray-800">
    <div className="flex flex-row h-full w-full overflow-x-hidden">
      <div className="flex flex-col py-8 pl-6 pr-2 w-64 bg-black flex-shrink-0">
        <div className="flex flex-row items-center justify-center h-12 w-full">
          <div
            className="flex items-center justify-center rounded-2xl text-indigo-700 bg-indigo-100 h-10 w-10"
          >
            <svg
              className="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
              ></path>
            </svg>
          </div>
          <div className="ml-2 font-bold text-2xl text-white">QuickChat</div>
        </div>
        <div
          className="flex flex-col items-center bg-indigo-100 border border-gray-200 mt-4 w-full py-6 px-4 rounded-lg"
        >
          <div className="h-20 w-20 rounded-full border overflow-hidden">
            <img
              src="https://avatars3.githubusercontent.com/u/2763884?s=128"
              alt="Avatar"
              className="h-full w-full"
            />
          </div>
          <div className="text-sm font-semibold mt-2">DELTA</div>
          <div className="text-xs text-gray-500">GENERATIVE AI Expert</div>
          <div className="flex flex-row items-center mt-3">
            <div
              className="flex flex-col justify-center h-4 w-8 bg-indigo-500 rounded-full"
            >
              <div className="h-3 w-3 bg-white rounded-full self-end mr-1"></div>
            </div>
            <div className="leading-none ml-1 text-xs">Active</div>
          </div>
        </div>
        <div className="flex flex-col mt-8">
          <div className="flex flex-row items-center justify-between text-xs">
            <span className="font-bold text-white ">History</span>
            <span
              className="flex items-center justify-center bg-gray-300 h-4 w-4 rounded-full"
              >4</span>
          </div>
          <div className="flex flex-col space-y-1 mt-4 -mx-2 h-48 overflow-y-auto">
            <button
              className="flex flex-row items-center hover:bg-purple-300 rounded-xl p-2"
            >
              <div className="ml-2 text-sm font-semibold text-white">Polynomials</div>
            </button>
            <button
              className="flex flex-row items-center hover:bg-purple-300 rounded-xl p-2"
            >
              
              <div className="ml-2 text-sm font-semibold text-white">Exponents</div>
            </button>
            <button
              className="flex flex-row items-center hover:bg-purple-300 rounded-xl p-2"
            >
              <div className="ml-2 text-sm font-semibold text-white">Linear Equations</div>
            </button>
            <button
              className="flex flex-row items-center hover:bg-purple-300 rounded-xl p-2"
            >
              <div className="ml-2 text-sm font-semibold text-white">Factorization</div>
            </button>
            <button
              className="flex flex-row items-center hover:bg-purple-300 rounded-xl p-2"
            >
              <div className="ml-2 text-sm font-semibold text-white">Factorization Equations</div>
            </button>
          </div>
          <div className="flex flex-row items-center justify-between text-xs mt-6">
            <span className="font-bold text-white">Archivied</span>
            <span
              className="flex items-center justify-center bg-gray-300 h-4 w-4 rounded-full"
              >7</span>
          </div>
          <div className="flex flex-col space-y-1 mt-4 -mx-2">
            <button
              className="flex flex-row items-center hover:bg-gray-100 rounded-xl p-2"
            >
              <div className="ml-2 text-sm font-semibold text-white">Henry Boyd</div>
            </button>
          </div>
        </div>
      </div>
      <div className="flex flex-col flex-auto h-full p-6">
        <div
          className="flex flex-col flex-auto flex-shrink-0 rounded-2xl bg-gradient-to-tr from-slate-900 to-purple-400 h-full p-4"
        >
          <div className="flex flex-col h-full overflow-x-auto mb-4">
            <div className="flex flex-col h-full">
              <div className="grid grid-cols-12 gap-y-2">
              {messages.map((message, index) => (
                    <div key={index} className="col-start-1 col-end-8 p-3 rounded-lg">
                      <div className="flex flex-row items-center">
                        <div className="relative ml-3 text-sm it bg-white py-2 px-4 shadow rounded-xl ">
                          <div>{message}</div>
                        </div>
                      </div>
                    </div>
                  ))}
              </div>
            </div>
          </div>
          <div
            className="flex flex-row items-center h-16 rounded-xl bg-white w-full px-4"
          >
            <div>
              <button
                className="flex items-center justify-center text-gray-400 hover:text-gray-600"
              >
                <img src="keyboard.png" className="h-9 w-9" >
                </img>
              </button>
            </div>
            <div className="flex-grow ml-4">
              <div className="relative w-full">
                <input
                  type="text"
                  placeholder="Enter your Problem ...... "
                  className="flex w-full border rounded-xl  focus:outline-none focus:border-indigo-300 pl-4 h-10"
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  onKeyPress={handleKeyPress}
                />
              </div>
            </div>
            <div className="ml-4">
              
              <button
                  className="flex items-center justify-center bg-indigo-500 hover:bg-indigo-600 rounded-xl text-white px-4 py-1 flex-shrink-0"
                  onClick={handleSend}
                >
                  <span>Send</span>
                  <span className="ml-2">
                    <svg
                      className="w-4 h-4 transform rotate-45 -mt-px"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                      ></path>
                    </svg>
                  </span>
              </button>

            </div>
            <button
                className="flex items-center justify-center bg-red-500 hover:bg-red-600 rounded-xl text-white px-4 py-1 flex-shrink-0"
                onClick={handleClearChat}
              >
                <span>Clear Chat</span>
              </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  )
}

export default page