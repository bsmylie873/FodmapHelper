import React from 'react';
import { Link } from 'react-router-dom';
import { GithubIcon, InfoIcon } from 'lucide-react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gray-100 border-t border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div className="md:flex md:items-center md:justify-between">
          <div className="flex justify-center md:justify-start space-x-6">
            <a
              href="https://github.com"
              target="_blank"
              rel="noopener noreferrer"
              className="text-gray-600 hover:text-gray-900"
            >
              <span className="sr-only">GitHub</span>
              <GithubIcon className="h-5 w-5" />
            </a>
            <Link to="/about" className="text-gray-600 hover:text-gray-900 flex items-center space-x-1">
              <InfoIcon className="h-5 w-5" />
              <span>About</span>
            </Link>
          </div>
          <div className="mt-4 md:mt-0">
            <p className="text-center md:text-right text-sm text-gray-500">
              &copy; {new Date().getFullYear()} FODMAP Helper. All rights
              reserved.
            </p>
            <p className="text-center md:text-right text-xs text-gray-400 mt-1">
              <Link to="/about" className="hover:underline">
                License Info
              </Link>
              {' • '}
              <Link to="/about" className="hover:underline">
                Contribute
              </Link>
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 