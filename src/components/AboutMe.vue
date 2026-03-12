<template>
  <section class="rounded-lg bg-slate-100 dark:bg-dark-card p-8 md:p-10">
    <div class="flex flex-col items-center gap-8 md:flex-row md:items-start">
      <div class="flex h-36 w-36 shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-primary to-secondary shadow-lg overflow-hidden">
        <img src="../assets/images/me_logo.jpg" alt="Jeremy Lankford" class="h-full w-full object-cover" />
      </div>

      <div class="flex-1 text-center md:text-left">
        <h2 class="mb-2 text-3xl font-bold text-slate-900 md:text-4xl dark:text-white">Jeremy Lankford</h2>
        <p class="mb-5 text-lg font-medium text-slate-600 dark:text-slate-400">Senior Software Engineer & Aspiring IT Educator</p>
        
        <div class="space-y-4 text-base leading-relaxed text-slate-600 md:text-lg dark:text-slate-400">
          <p>
            With over 30 years in software development, from Java and C++ to modern Vue and React, I specialize in full-stack architecture and cloud-native solutions.
          </p>
          <p>
            I am completing my MBA in IT Management and preparing for doctoral studies in AI, with a strong focus on leadership, performance management systems, and mentoring the next generation of developers.
          </p>
        </div>

        <div class="mt-7 flex flex-wrap justify-center gap-2 md:justify-start">
          <span class="rounded-full bg-primary/10 px-3 py-1 text-xs font-semibold text-primary dark:bg-primary/20 dark:text-indigo-300">Software Architecture</span>
          <span class="rounded-full bg-secondary/10 px-3 py-1 text-xs font-semibold text-secondary dark:bg-secondary/20 dark:text-purple-300">AI Education</span>
          <span class="rounded-full bg-teal-500/10 px-3 py-1 text-xs font-semibold text-teal-600 dark:bg-teal-500/20 dark:text-teal-300">IT Leadership</span>
        </div>

        <div class="mt-8 pt-6 border-t border-slate-200 dark:border-slate-700">
          <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-4 text-center md:text-left">Education</h3>
          <ul class="text-base leading-relaxed text-slate-600 md:text-lg dark:text-slate-400 space-y-6">
            <li class="flex items-center gap-4">
              <div class="h-14 w-14 shrink-0 bg-white rounded-md flex items-center justify-center p-1.5 shadow-sm border border-slate-200">
                <img src="../assets/logos/uoc.png" alt="University of the Cumberlands Logo" class="h-full w-full object-contain" />
              </div>
              <div>
                <span class="block font-semibold text-slate-800 dark:text-slate-200">Doctoral Candidate in Information Technology</span>
                <span class="block text-sm text-slate-500 dark:text-slate-400">Concentration in Artificial Intelligence</span>
                <a href="https://www.ucumberlands.edu/" target="_blank" rel="noopener noreferrer" class="block text-sm font-medium text-primary hover:text-secondary transition mt-1">University of the Cumberlands</a>
              </div>
            </li>
            <li class="flex items-center gap-4">
              <div class="h-14 w-14 shrink-0 bg-white rounded-md flex items-center justify-center p-1.5 shadow-sm border border-slate-200">
                <img src="../assets/logos/snhu.png" alt="SNHU Logo" class="h-full w-full object-contain" />
              </div>
              <div>
                <span class="block font-semibold text-slate-800 dark:text-slate-200">Master's of Business Administration</span>
                <span class="block text-sm text-slate-500 dark:text-slate-400">Concentration in IT Management</span>
                <a href="https://www.snhu.edu/" target="_blank" rel="noopener noreferrer" class="block text-sm font-medium text-primary hover:text-secondary transition mt-1">Southern New Hampshire University</a>
              </div>
            </li>
            <li class="flex items-center gap-4">
              <div class="h-14 w-14 shrink-0 bg-white rounded-md flex items-center justify-center p-1.5 shadow-sm border border-slate-200">
                <img src="../assets/logos/PurdueGlobal.webp" alt="Purdue Global Logo" class="h-full w-full object-contain" />
              </div>
              <div>
                <span class="block font-semibold text-slate-800 dark:text-slate-200">Bachelor's Degree in Information Technology</span>
                <span class="block text-sm text-slate-500 dark:text-slate-400">Concentration in Software Development with Python</span>
                <a href="https://www.purdueglobal.edu/" target="_blank" rel="noopener noreferrer" class="block text-sm font-medium text-primary hover:text-secondary transition mt-1">Purdue Global</a>
              </div>
            </li>
            <li class="pt-2">
              <span><a href="https://www.coursera.org/user/b6fd93fb723fe10904a3c042504e0386" target="_blank" rel="noopener noreferrer" class="font-medium text-primary hover:text-secondary underline transition">Official Coursera Transcript</a></span>
            </li>
          </ul>
        </div>

        <div class="mt-8 pt-6 border-t border-slate-200 dark:border-slate-700">
          <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-4 text-center md:text-left">Certificates</h3>
          <ul class="text-base leading-relaxed text-slate-600 md:text-lg dark:text-slate-400 space-y-4">
            <li class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-100 dark:border-slate-800 pb-3 last:border-0">
              <div class="flex items-center gap-4">
                <div class="h-10 w-10 shrink-0 flex items-center justify-center p-1 border border-slate-200 rounded bg-white">
                  <img src="../assets/logos/Azure-AI-Engineer-Associate-Course.jpg" alt="Azure AI Engineer Associate Logo" class="h-full w-full object-contain" />
                </div>
                <div>
                  <span class="block font-semibold text-slate-800 dark:text-slate-200">Azure AI Engineer Associate (AI-102)</span>
                  <span class="block text-sm text-slate-500 dark:text-slate-400">Microsoft</span>
                </div>
              </div>
              <a href="https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/" target="_blank" rel="noopener noreferrer" class="text-sm font-medium text-primary hover:text-secondary whitespace-nowrap transition flex items-center gap-1.5 mt-2 md:mt-0 ml-14 md:ml-0">
                View Details <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
              </a>
            </li>
            <li class="flex flex-col gap-1 border-b border-slate-100 dark:border-slate-800 pb-3 last:border-0">
              <div class="flex items-center gap-4">
                <div class="h-10 w-10 shrink-0 flex items-center justify-center p-1 border border-slate-200 rounded bg-white">
                  <img src="../assets/logos/google.png" alt="Google Logo" class="h-full w-full object-contain" />
                </div>
                <div>
                  <span class="block font-semibold text-slate-800 dark:text-slate-200">Google Cloud Generative AI Leader</span>
                </div>
              </div>
              <div class="flex items-center justify-between">
                <span class="block text-sm text-slate-500 dark:text-slate-400">Professional Certificate</span>
                <a href="https://www.coursera.org/user/b6fd93fb723fe10904a3c042504e0386" target="_blank" rel="noopener noreferrer" class="text-sm font-medium text-primary hover:text-secondary whitespace-nowrap transition flex items-center gap-1.5">
                  View Certificate <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                </a>
              </div>
            </li>
            <li class="flex flex-col gap-1 border-b border-slate-100 dark:border-slate-800 pb-3 last:border-0">
              <div class="flex items-center gap-4">
                <div class="h-10 w-10 shrink-0 flex items-center justify-center p-1 border border-slate-200 rounded bg-white">
                  <img src="../assets/logos/google.png" alt="Google Logo" class="h-full w-full object-contain" />
                </div>
                <div>
                  <span class="block font-semibold text-slate-800 dark:text-slate-200">Google Project Management</span>
                </div>
              </div>
              <div class="flex items-center justify-between">
                <span class="block text-sm text-slate-500 dark:text-slate-400">Professional Certificate</span>
                <a href="https://www.coursera.org/user/b6fd93fb723fe10904a3c042504e0386" target="_blank" rel="noopener noreferrer" class="text-sm font-medium text-primary hover:text-secondary whitespace-nowrap transition flex items-center gap-1.5">
                  View Certificate <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                </a>
              </div>
            </li>
            <li class="flex flex-col gap-1 border-b border-slate-100 dark:border-slate-800 pb-3 last:border-0">
              <div class="flex items-center gap-4">
                <div class="h-10 w-10 shrink-0 flex items-center justify-center p-1 border border-slate-200 rounded bg-white">
                  <img src="../assets/logos/google.png" alt="Google Logo" class="h-full w-full object-contain" />
                </div>
                <div>
                  <span class="block font-semibold text-slate-800 dark:text-slate-200">Google IT Automation with Python</span>
                </div>
              </div>
              <div class="flex items-center justify-between">
                <span class="block text-sm text-slate-500 dark:text-slate-400">Professional Certificate</span>
                <a href="https://www.coursera.org/user/b6fd93fb723fe10904a3c042504e0386" target="_blank" rel="noopener noreferrer" class="text-sm font-medium text-primary hover:text-secondary whitespace-nowrap transition flex items-center gap-1.5">
                  View Certificate <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                </a>
              </div>
            </li>
            <li class="flex flex-col gap-1 border-b border-slate-100 dark:border-slate-800 pb-3 last:border-0">
              <div class="flex items-center gap-4">
                <div class="h-10 w-10 shrink-0 flex items-center justify-center p-1 border border-slate-200 rounded bg-white">
                  <img src="../assets/logos/hrci.png" alt="HRCI Logo" class="h-full w-full object-contain" />
                </div>
                <div>
                  <span class="block font-semibold text-slate-800 dark:text-slate-200">HRCI Human Resource Associate</span>
                </div>
              </div>
              <div class="flex items-center justify-between">
                <span class="block text-sm text-slate-500 dark:text-slate-400">Professional Certificate</span>
                <a href="https://www.coursera.org/user/b6fd93fb723fe10904a3c042504e0386" target="_blank" rel="noopener noreferrer" class="text-sm font-medium text-primary hover:text-secondary whitespace-nowrap transition flex items-center gap-1.5">
                  View Certificate <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                </a>
              </div>
            </li>
            <li class="flex flex-col gap-1 border-b border-slate-100 dark:border-slate-800 pb-3 last:border-0">
              <div class="flex items-center gap-4">
                <div class="h-10 w-10 shrink-0 flex items-center justify-center p-1 border border-slate-200 rounded bg-white">
                  <img src="../assets/logos/meta.png" alt="Meta Logo" class="h-full w-full object-contain" />
                </div>
                <div>
                  <span class="block font-semibold text-slate-800 dark:text-slate-200">Meta Front-End Developer</span>
                </div>
              </div>
              <div class="flex items-center justify-between">
                <span class="block text-sm text-slate-500 dark:text-slate-400">Professional Certificate</span>
                <a href="https://www.coursera.org/account/accomplishments/professional-cert/GRXL3YYPUHZX" target="_blank" rel="noopener noreferrer" class="text-sm font-medium text-primary hover:text-secondary whitespace-nowrap transition flex items-center gap-1.5">
                  View Certificate <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                </a>
              </div>
            </li>
          </ul>
        </div>

        <div class="mt-8 pt-6 border-t border-slate-200 dark:border-slate-700">
          <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-4 text-center md:text-left">Specializations</h3>
          <ul class="text-base leading-relaxed text-slate-600 md:text-lg dark:text-slate-400 space-y-4">
            <li class="flex flex-col gap-1 border-b border-slate-100 dark:border-slate-800 pb-3 last:border-0">
              <div class="flex items-center gap-4">
                <div class="h-10 w-10 shrink-0 flex items-center justify-center p-1 border border-slate-200 rounded bg-white">
                  <img src="../assets/logos/MM.png" alt="Macquarie University Logo" class="h-full w-full object-contain" />
                </div>
                <div>
                  <span class="block font-semibold text-slate-800 dark:text-slate-200">Online Learning Design for Educators</span>
                  <span class="block text-base font-medium text-slate-700 dark:text-slate-300">Macquarie University</span>
                </div>
              </div>
              <div class="flex items-center justify-between">
                <span class="block text-sm text-slate-500 dark:text-slate-400">Specialization</span>
                <a href="https://www.coursera.org/user/b6fd93fb723fe10904a3c042504e0386" target="_blank" rel="noopener noreferrer" class="text-sm font-medium text-primary hover:text-secondary whitespace-nowrap transition flex items-center gap-1.5">
                  View Certificate <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                </a>
              </div>
            </li>
            <li class="flex flex-col gap-1 border-b border-slate-100 dark:border-slate-800 pb-3 last:border-0">
              <div class="flex items-center gap-4">
                <div class="h-10 w-10 shrink-0 flex items-center justify-center p-1 border border-slate-200 rounded bg-white">
                  <img src="../assets/logos/UoP.png" alt="University of Pennsylvania Logo" class="h-full w-full object-contain" />
                </div>
                <div>
                  <span class="block font-semibold text-slate-800 dark:text-slate-200">Achieving Personal and Professional Success</span>
                  <span class="block text-base font-medium text-slate-700 dark:text-slate-300">University of Pennsylvania</span>
                </div>
              </div>
              <div class="flex items-center justify-between">
                <span class="block text-sm text-slate-500 dark:text-slate-400">Specialization</span>
                <a href="https://www.coursera.org/user/b6fd93fb723fe10904a3c042504e0386" target="_blank" rel="noopener noreferrer" class="text-sm font-medium text-primary hover:text-secondary whitespace-nowrap transition flex items-center gap-1.5">
                  View Certificate <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                </a>
              </div>
            </li>
            <li class="flex flex-col gap-1 border-b border-slate-100 dark:border-slate-800 pb-3 last:border-0">
              <div class="flex items-center gap-4">
                <div class="h-10 w-10 shrink-0 flex items-center justify-center p-1 border border-slate-200 rounded bg-white">
                  <img src="../assets/logos/UoP.png" alt="University of Pennsylvania Logo" class="h-full w-full object-contain" />
                </div>
                <div>
                  <span class="block font-semibold text-slate-800 dark:text-slate-200">Business Foundations</span>
                  <span class="block text-base font-medium text-slate-700 dark:text-slate-300">University of Pennsylvania</span>
                </div>
              </div>
              <div class="flex items-center justify-between">
                <span class="block text-sm text-slate-500 dark:text-slate-400">Specialization</span>
                <a href="https://www.coursera.org/user/b6fd93fb723fe10904a3c042504e0386" target="_blank" rel="noopener noreferrer" class="text-sm font-medium text-primary hover:text-secondary whitespace-nowrap transition flex items-center gap-1.5">
                  View Certificate <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                </a>
              </div>
            </li>
          </ul>

          <div class="mt-8 flex justify-center md:justify-start">
            <a href="https://www.credly.com/users/jeremy-lankford.5881bd2a/badges#credly" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 rounded-lg bg-[#FF6B00] px-5 py-2.5 text-sm font-bold text-white shadow-md transition hover:bg-[#e66100]">
              <svg role="img" viewBox="0 0 24 24" class="h-5 w-5 fill-current" xmlns="http://www.w3.org/2000/svg">
                <path d="M23.8 13.154a.299.299 0 0 0-.101-.024.407.407 0 0 0-.202.048c-.06.028-.092.08-.127.136-.087.128-.15.268-.226.4-.107.187-.246.351-.38.515-.135.156-.286.291-.424.44-.028.027-.072.043-.107.027-.028-.016-.036-.056-.032-.088.04-.38.075-.763.123-1.138.02-.172.043-.336.063-.512.028-.247.056-.487.087-.735l.234-1.824c.02-.128.032-.372-.135-.52a.446.446 0 0 0-.233-.116.46.46 0 0 0-.254.06c-.226.16-.297.504-.365.76-.142.603-.178 1.241-.471 1.804a1.772 1.772 0 0 1-.202.316.668.668 0 0 1-.186.18.332.332 0 0 1-.246.051.365.365 0 0 1-.238-.207.871.87 0 0 1-.063-.324 4.499 4.499 0 0 1 .24-1.585c.045-.132.089-.252.104-.383.028-.156.028-.38-.114-.516-.131-.128-.337-.18-.504-.128-.194.056-.31.244-.372.392-.198.463-.25.95-.317 1.446-.044.327-.127.64-.293.926a2.717 2.717 0 0 1-.603.72c-.118.087-.222.123-.328.107a.376.376 0 0 1-.278-.208.875.875 0 0 1-.095-.315 3.361 3.36 0 0 1-.036-.616c.004-.223 0-.44.044-.658.075-.39.678-1.937.808-2.345.135-.407.262-.823.353-1.246.08-.38.123-.767.11-1.15-.007-.277-.07-.576-.288-.736a.611.61 0 0 0-.603-.048.968.968 0 0 0-.455.428 2.53 2.53 0 0 0-.226.59 12.01 12.01 0 0 0-.266 1.29c-.071.429-.138.848-.206 1.268-.06.355-.206 1.614-.261 1.88-.06.272-.175.54-.301.787-.131.268-.258.536-.408.791a.694.694 0 0 1-.175.224c-.08.06-.182.088-.27.048-.102-.048-.146-.176-.166-.292-.075-.435-.012-.875.072-1.302.083-.431.44-2.4.519-2.851.099-.532.24-1.05.285-1.59.028-.388.09-.88-.202-1.187-.115-.136-.31-.16-.44-.136-.174.036-.31.176-.388.296-.1.128-.186.28-.258.467-.115.284-.186.615-.261.91l-.032.129c-.083.383-.143.77-.186 1.162a16.95 16.948 0 0 0-.06.632c-.008.1-.016.203-.027.307 0 .08.007.168-.028.244a.304.304 0 0 1-.052.068c-.08.072-.202.06-.31.056-.557-.016-1.045.3-1.35.755-.18.252-.281.542-.39.834-.01.048-.034.1-.054.152-.051.143-.13.327-.222.511a3.037 3.037 0 0 1-.317.46 3.285 3.285 0 0 1-.384.41 1.123 1.123 0 0 1-.515.26c-.174.04-.384-.043-.543-.203a.916.916 0 0 1-.206-.54c-.004-.055-.004-.115.028-.163.05-.068.146-.072.23-.076a1.623 1.623 0 0 0 1.375-1.015c.138-.34.178-.698.122-1.046a1.193 1.193 0 0 0-.19-.48.9.9 0 0 0-.396-.323c-.293-.14-.658-.127-1.01.004-.575.232-.951.74-1.134 1.562l-.02.088c-.114.487-.23 1-.582 1.354-.127.12-.261.163-.368.143-.044-.004-.08-.04-.103-.075-.096-.16.003-.532.15-1a4.1 4.1 0 0 0 .1-.366.925.925 0 0 0-.108-.495.783.783 0 0 0-.372-.324c-.143-.064-.31-.06-.468-.06h-.047c-.044 0-.103 0-.151-.012a.215.215 0 0 1-.147-.127.485.485 0 0 1 .016-.232c.004-.02.012-.048.016-.072a.368.368 0 0 0-.162-.412.509.509 0 0 0-.468-.036.768.768 0 0 0-.364.348.769.769 0 0 0-.103.48c.04.13.07.32.043.475-.055.28-.222.51-.384.74-.04.05-.072.106-.107.16a4.96 4.96 0 0 1-.706.825c-.372.335-.804.575-1.232.67-.745.165-1.506-.06-1.91-.734-.222-.38-.32-.827-.348-1.266a5.425 5.425 0 0 1 .424-2.516c.328-.76.816-1.52 1.715-1.614.353-.04.753.083.912.4.115.23.075.506 0 .75-.072.244-.175.49-.18.75-.003.26.124.54.37.616.238.072.495-.08.634-.29.138-.21.186-.46.245-.704a6.282 6.281 0 0 1 .662-1.634c.139-.236.297-.488.254-.76a.543.543 0 0 0-.373-.415.543.543 0 0 0-.535.144c-.134.148-.206.371-.387.43-.17.06-.35-.055-.507-.134-.6-.32-1.336-.312-1.963-.048-.634.25-1.146.735-1.526 1.294C.462 8.53.098 9.508.022 10.48c-.027.34-.031.695 0 1.038.036.46.1.854.214 1.206.139.423.317.79.547 1.094.266.34.587.6.94.747.372.148.784.22 1.192.208a3.172 3.172 0 0 0 1.177-.283 4.29 4.29 0 0 0 1.026-.68c.309-.26.594-.559.84-.89.162-.224.309-.46.44-.708a4.83 4.83 0 0 0 .178-.383c.044-.104.087-.215.202-.26.056-.043.15-.02.202.013.064.04.115.075.135.135.048.116.02.232-.004.332v.012c-.028.1-.055.203-.091.303-.14.424-.238.811-.16 1.195.045.207.128.387.25.527a.84.84 0 0 0 .504.264c.246.04.51-.028.725-.132.143-.068.278-.156.397-.26.06-.06.122-.12.174-.184.044-.06.087-.147.178-.143a.15.15 0 0 1 .107.064c.028.031.04.071.06.115.23.52.776.84 1.335.84h.07c.27 0 .556-.093.79-.22.27-.14.48-.348.7-.552.02-.016.045-.04.073-.044.035-.008.07.012.099.044a.26.26 0 0 1 .047.1c.135.34.46.6.824.66a1.1 1.1 0 0 0 .99-.356c.056-.06.104-.128.167-.176.064-.044.15-.076.222-.044.107.04.135.164.182.268.107.235.357.371.615.375.289 0 .554-.148.764-.34.195-.183.353-.399.516-.61a.328.328 0 0 1 .106-.096c.04-.024.096-.028.13 0 .033.024.045.06.06.091.163.4.587.652 1.01.648.417-.004.809-.224 1.103-.516.095-.092.194-.2.32-.21.14-.017.207.114.254.22.072.142.115.238.25.338.158.116.36.152.547.1.17-.04.34-.156.47-.316.072-.088.112-.204.19-.284.092-.087.132.028.136.1.016.116.016.236.008.352-.016.236-.052.471-.08.703-.011.068-.02.136-.063.188-.06.068-.166.08-.253.064a2.898 2.898 0 0 0-.321-.028l-.14-.016c-.201-.012-.4-.036-.61-.044h-.185c-.404 0-.733.048-1.03.16-.48.187-.852.57-1.003 1.018a1.305 1.305 0 0 0-.052.64c.04.203.13.403.282.587.265.315.68.515 1.149.543.408.02.852-.064 1.292-.26.848-.367 1.482-1.094 1.696-1.95 0-.02.01-.039.023-.043.298-.104.57-.248.813-.428.245-.187.467-.399.65-.643.09-.12.174-.243.253-.37.07-.125.13-.257.202-.38a.906.906 0 0 0 .13-.316.411.411 0 0 0-.05-.328.257.257 0 0 0-.135-.124m-13.68-1.63c.017-.071.045-.14.06-.206a1.9 1.9 0 0 1 .262-.504c.04-.048.08-.1.135-.136a.246.246 0 0 1 .186-.048c.107.02.183.128.202.236.032.18-.04.396-.114.555a1.097 1.097 0 0 1-.31.415c-.06.044-.114.088-.178.116-.028.008-.063.028-.115.028h-.016c-.055 0-.114-.028-.126-.088a.827.827 0 0 1 .015-.367m4.308-.184c-.004.072-.024.148-.028.223a4.91 4.91 0 0 0 0 .779c.012.152.047.3-.016.444a1.069 1.069 0 0 1-.567.643.555.555 0 0 1-.245.056c-.02 0-.04-.004-.06-.004-.12 0-.214-.092-.265-.18a.871.87 0 0 1-.1-.272 2.129 2.129 0 0 1 .072-1.122c.08-.22.202-.435.38-.594a.874.874 0 0 1 .563-.24.31.31 0 0 1 .206.064c.04.044.06.104.056.164a.05.05 0 0 1 .004.04m6.43 4.653c-.015.044-.06.104-.08.14-.042.08-.102.163-.161.235a2.562 2.562 0 0 1-.317.304c-.238.18-.503.311-.777.387a2.025 2.025 0 0 1-.487.072h-.04a.795.795 0 0 1-.515-.18.433.433 0 0 1-.158-.25.537.537 0 0 1 .047-.305.776.776 0 0 1 .38-.383c.326-.16.682-.176 1.019-.16.139.004.265.012.4.02.107.004.218.012.325.024.056 0" />
              </svg>
              View on Credly
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>