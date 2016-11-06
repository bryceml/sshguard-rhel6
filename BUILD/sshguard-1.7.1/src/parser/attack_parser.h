#define IPv4 257
#define IPv6 258
#define HOSTADDR 259
#define WORD 260
#define INTEGER 261
#define SYSLOG_BANNER_PID 262
#define SOCKLOG_BANNER_PID 263
#define LAST_LINE_REPEATED_N_TIMES 264
#define SYSLOG_BANNER 265
#define TIMESTAMP_SYSLOG 266
#define TIMESTAMP_ISO8601 267
#define TIMESTAMP_TAI64 268
#define AT_TIMESTAMP_TAI64 269
#define METALOG_BANNER 270
#define SOCKLOG_BANNER 271
#define SSH_INVALUSERPREF 272
#define SSH_NOTALLOWEDPREF 273
#define SSH_NOTALLOWEDSUFF 274
#define SSH_LOGINERR_PREF 275
#define SSH_LOGINERR_SUFF 276
#define SSH_LOGINERR_PAM 277
#define SSH_VIA 278
#define SSH_NOIDENTIFSTR 279
#define SSH_BADPROTOCOLIDENTIF 280
#define SSH_BADPROTOCOLIDENTIF_SUFF 281
#define SSH_BADKEX_PREF 282
#define SSH_BADKEX_SUFF 283
#define SSH_DISCONNECT_PREF 284
#define SSH_PREAUTH_SUFF 285
#define DOVECOT_IMAP_LOGINERR_PREF 286
#define DOVECOT_IMAP_LOGINERR_SUFF 287
#define UWIMAP_LOGINERR 288
#define CYRUSIMAP_SASL_LOGINERR_PREF 289
#define CYRUSIMAP_SASL_LOGINERR_SUFF 290
#define CUCIPOP_AUTHFAIL 291
#define EXIM_ESMTP_AUTHFAIL_PREF 292
#define EXIM_ESMTP_AUTHFAIL_SUFF 293
#define SENDMAIL_RELAYDENIED_PREF 294
#define SENDMAIL_RELAYDENIED_SUFF 295
#define SENDMAIL_AUTHFAILURE_PREF 296
#define SENDMAIL_AUTHFAILURE_SUFF 297
#define POSTFIX_NO_AUTH_PREF 298
#define POSTFIX_SASL_LOGINERR_PREF 299
#define POSTFIX_SASL_LOGINERR_SUFF 300
#define FREEBSDFTPD_LOGINERR_PREF 301
#define FREEBSDFTPD_LOGINERR_SUFF 302
#define PROFTPD_LOGINERR_PREF 303
#define PROFTPD_LOGINERR_SUFF 304
#define PUREFTPD_LOGINERR_PREF 305
#define PUREFTPD_LOGINERR_SUFF 306
#define VSFTPD_LOGINERR_PREF 307
#define VSFTPD_LOGINERR_SUFF 308
#ifdef YYSTYPE
#undef  YYSTYPE_IS_DECLARED
#define YYSTYPE_IS_DECLARED 1
#endif
#ifndef YYSTYPE_IS_DECLARED
#define YYSTYPE_IS_DECLARED 1
typedef union {
    char *str;
    int num;
} YYSTYPE;
#endif /* !YYSTYPE_IS_DECLARED */
extern YYSTYPE yylval;
